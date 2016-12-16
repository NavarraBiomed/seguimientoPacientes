"use strict"

class Filter{
    constructor(field, value){
        this.field = field;
        this.value = value;
    }

    apply(elements){

        var filter = this;
        var filteredIn = [];
        $(elements).find(".row-data").each(function(){
            if ( $(this).find(".data[data-"+filter.field+"="+filter.value+"]").length != 1){
                $(this).closest(".patient-row").addClass("filteredOut");
            } else{
                filteredIn.push($(this).closest(".patient-row")[0]);
            }

        });
        return filteredIn;


    }

    equals(other){
        return this.field == other.field && this.value == other.value;
    }

    setValue(value){
        this.value = value;
    }

    getValue(){
        return this.value;
    }

}

class FilterEngine{
    constructor(elements){
        this.filters =[];
        this.elements = elements;
        this.activeElements = this.elements;
    }

    selectFilter(field){
        for (var i=0; i< this.filters.length; i++){
            if (this.filters[i].field == field){
                return this.filters[i];
            }
        }
        return;
    }

    reset(){
        for (var i=0; i < this.elements.length; i++){
            var element = this.elements[i];
            $(element).removeClass("filteredOut");
        }
        this.activeElements = this.elements;


    }

    removeFilter(filter){
        var index = this.filters.indexOf(filter);
        this.filters.splice(index, 1);
    }

    applyFilters(){
        this.reset();
        this.print();
        for (var i=0; i< this.filters.length; i++){
            this.activeElements = this.filters[i].apply(this.activeElements);
        }
    }

    addFilter(field, value){

        var filter = this.selectFilter(field);
        if ( filter == undefined){
            if (value != ""){
                filter = new Filter(field, value);
                this.filters.push(filter);
                this.applyFilters();
            }
        } else{
            if (value == ""){
                this.removeFilter(filter);
                this.applyFilters();
            } else if( value != filter.getValue()){
                filter.setValue(value);
                this.applyFilters();
            }

        }
    }

    print(){
        console.log("-----Filters----");
        for (var i=0; i< this.filters.length; i++){
            console.log(this.filters[i].field +"|"+this.filters[i].value);
        }
        console.log("----------------");
    }


}


var filterEngine;
$(document).ready(function(){

    filterEngine = new FilterEngine($(".patient-row"));

    $(".filter-input").on("change keyup paste", function(){
        var field = $(this).attr("data-field");
        var value = $(this).val();

        filterEngine.addFilter( field, value );

    })


});
