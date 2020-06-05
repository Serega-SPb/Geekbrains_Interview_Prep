
window.onload = function(){
    var modal = document.getElementById("modal-win");
    var open_btn = document.getElementById("open-modal");
    var open_btn_ajax = document.getElementById("open-modal-ajax");
    var close_btn = document.getElementById("close-modal");
    var add_form = document.getElementById("add-form");

    open_btn.addEventListener('click', ()=> {modal.style.display = 'block'})
    open_btn_ajax.addEventListener('click', ()=> {
        modal.style.display = 'block';
        add_form.removeAttribute('action');
        var save_btn = document.getElementById('save-modal');
        save_btn.type = 'button'
        save_btn.addEventListener('click', ajaxSubmit);
        save_btn.addEventListener('click', ()=> {close_btn.click()});
    })
    close_btn.addEventListener('click', ()=> {modal.style.display = 'none'})
}

function ajaxSubmit(){
    $.ajax({
        url: "/add_ajax/",
        type: "POST",
        data: getFormData(),
        processData: false,
        contentType: false,
        success: (answer) => {
            if (answer['result'] === 'OK')
                reloadItems();
        }
    });
}

function getFormData(){
    var form_data = new FormData();
    var inputs = $('#add_form, input');
    for (var i=0; i < inputs.length; i++){
        inp = inputs[i]
        if (inp.type !== 'file')
            form_data.append(inp.name, inp.value);
        else
            form_data.append(inp.name, inp.files[0]);
    }
    return form_data
}

function reloadItems(){
    $.ajax({
        url: '/update_items/',
        success: (answer) =>{
            var new_html = $(answer);
            $('#items-tbl').html(new_html.find('#items-tbl').html());
        }
    })
}