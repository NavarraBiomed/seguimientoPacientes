from django.core.management.base import BaseCommand, CommandError
from django.db.models.fields.related import ForeignKey,ManyToOneRel, ManyToManyRel
from ictus.models import *
from savReaderWriter import SavReader

DEBUG = False

var_dict = {}


def debug(message):
    if DEBUG:
        print(message)

def get_var(line, var):
    var = var.lower()
    if var in var_dict:
        result = line[var_dict[var]]

        if type(result) == bytes:
            try:
                result = result.decode("latin-1", "replace")
            except Exception:
                print("Error decoding bytes")
                exit()


        return result
    else:
        return None


def get_models_fields(model):
    fields_raw = model._meta.get_fields()
    fields = []
    for field in fields_raw:
        if type(field) not in [ForeignKey, ManyToOneRel, ManyToManyRel] :
            fields.append( str(field).split(".")[-1] )

    return fields


def add_patient(line):
    """
    Scans a line and checks if the NHC is already in the DB
    if so, returns that patient
    else, creates a new patient and returns it
    """
    try:
        paciente = Paciente.objects.get(nhc=get_var(line,"nhc"))
        print("Paciente ya existe: "+str(paciente) +" --------------------------")
        return paciente
    except Paciente.DoesNotExist:
        pass

    debug("Nuevo paciente: "+ str(round(get_var(line,"nhc"))) )

    paciente = Paciente()

    fields = get_models_fields(Paciente)

    for field in fields:
        value = get_var(line, field)
        if value is None:
            continue

        setattr(paciente, field, value )

    paciente.save()
    return paciente

def print_episode(episode):
    fields = get_models_fields(Episodio)
    for f in fields:
        print(str(f)+": " + str( getattr(episode,f)))

def add_episode(line, patient):
    """
    Scans a line and checks if the patient has an episode with the same date (fechaictus)
    if so, returns None (no additions needed)
    else, creates a new episode and returns it
    """
    try:
        episodio = Episodio.objects.get(paciente=patient, fechaictus=get_var(line,"fechaictus"))
        debug( "--Episodio ya existe: "+str(episodio) )
        return None
    except Episodio.DoesNotExist:
        pass

    debug("--Nuevo episodio: "+ str(get_var(line,"fechaictus")) )

    fields = get_models_fields(Episodio)

    episodio = Episodio()
    episodio.paciente = patient;

    for field in fields:
        value = get_var(line, field)
        if value is None:
            continue

        setattr(episodio, field, value )

    try:
        episodio.save()
        #print_episode(episodio)
    except TypeError:
        import pdb; pdb.set_trace()

    return episodio


def add_model(model_name, line, episode):
    """
    Adds a given model to an episode
    """
    if model_name == "Basal":
        model_class = Basal
    elif model_name == "Intervencion":
        model_class = Intervencion
    elif model_name == "Intraarterial":
        model_class = Intraarterial
    elif model_name =="Seguimiento":
        model_class = Seguimiento
    else:
        print("No existe el modelo: "+model_name)
        exit()

    model = model_class()
    model.episodio = episode

    fields = get_models_fields(model_class)

    for field in fields:
        value = get_var(line, field)

        if value is None:
            continue

        setattr(model, field, value )


    if 'recurrenciavascfecha' in fields: model.recurrenciavascfecha = None

    try:
        model.save()
    except TypeError:
        import pdb; pdb.set_trace()

    debug("----Nuevo "+model_name)
    return model


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('sav_file')
        parser.add_argument('--start', dest="start", default=False)
        parser.add_argument('--max_lines', dest="max_lines", default=False)

    def handle(self, *args, **options):

        file_name = options['sav_file']
        if options['start']:
            starting_line = int(options['start'])
        else:
            starting_line = 0

        if options['max_lines']:
            max_lines = int(options['max_lines'])
        else:
            max_lines = None

        #calculate the numnber of lines
        with SavReader(file_name) as reader:
            total_lines = 0
            for line in reader:
                total_lines += 1

            if max_lines is None:
                max_lines = total_lines

        with SavReader(file_name) as reader:

            #Make a dict with headers and numbers
            for i, field in enumerate(reader.header):
                var_dict[field.decode().lower()] = i

            current_line = -1
            percentage = 0

            for line in reader:
                current_line += 1
                if current_line < starting_line:
                    continue

                new_percentage = round( 100*(current_line - starting_line) / total_lines )
                if percentage != new_percentage:
                    percentage = new_percentage
                    print(str(percentage) +"% - line " + str(current_line - starting_line))

                if current_line - starting_line >= max_lines:
                    break

                patient = add_patient(line)
                episode = add_episode(line, patient)
                if episode is not None:
                    add_model("Basal", line, episode)
                    add_model("Intervencion", line, episode)
                    add_model("Seguimiento", line, episode)
