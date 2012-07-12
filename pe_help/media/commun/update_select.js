function UpdateSelect(objet, id_parent) {
    if (id_parent != 0){
        $.getJSON('/cj/getjson/' + objet + '/' + id_parent + '/', function(data){
            var newOptions = {};
            $.each(data, function(key, val) {
                newOptions[val.pk] = val.fields.titre;
            });
            var select = $('#' + objet);
            var options = select.prop('options');
            $('option', select).remove();

            options[0] = new Option('', 0);
            $.each(newOptions, function(key, val) {
                options[options.length] = new Option(val, key);
            });
            select.change();
        });
    }else{
        var select = $('#' + objet);
        var options = select.prop('options');
        $('option', select).remove();
    }
}
