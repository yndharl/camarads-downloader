var json = $.ajax({url:"/getPics", type: "GET", complete: function() {
    var cams = JSON.parse(json.responseText)
    for(pairIndex in cams){
        var inte = $('<div>', {id: 'internal'});
        inte.append(`<b>${cams[pairIndex].name}</b><br>`);
        for(roomIndex in cams[pairIndex].rooms){
            inte.append($("<img>", {
                src: cams[pairIndex].rooms[roomIndex].preview,
                id: "non-selected",
                click: toggleSelection,
                title: cams[pairIndex].rooms[roomIndex].title,
                stream: cams[pairIndex].rooms[roomIndex].stream
                }));
            }  
        $('#external').append(inte);
        }
    }
});
var streams = [];
$("#start-download").click(function(){
    $("[id=selected]").each(function(el){
        //console.log($(this).attr('stream'));
        streams.push($(this).attr('stream'));
        });
    $.ajax({url:"/sendStreams", type: "POST", data: {streams: JSON.stringify(streams)}});
});


function toggleSelection(){
    if(this.id=="non-selected"){
        this.id="selected";
    }
    else if(this.id=="selected") {
        this.id="non-selected";
    }
}

function download(data, filename){
    var file = new Blob([data], {type: 'application/json'});
    if (window.navigator.msSaveOrOpenBlob) // IE10+
        window.navigator.msSaveOrOpenBlob(file, filename);
    else { // Others
        var a = document.createElement("a"),
                url = URL.createObjectURL(file);
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        setTimeout(function() {
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);  
        }, 0); 
    }
}