function insert(event) {
    let formData = new FormData(event.currentTarget);
    let formDataObject = Object.fromEntries(formData.entries());
    let data = formDataObject;
    fetch("http://localhost:8080/insert", {
        method: "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(res => {
        console.log(res);
        if(res.ok) {
            alert("Usuario criado com sucesso");
            document.getElementById("formulario").reset();
        } else {
            alert("Erro ao cadastrar pessoa");
        }
    }).catch((_) => {
        alert("Erro ao criar pessoa")
    });
}

function select() {
    clear_list()
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:8080/select', true);
    xhr.responseType = 'json';
    xhr.onload = function() {
        if (xhr.status === 200) {
            console.log(null, xhr.response);
            fulfill_list(xhr.response);
        } else {
            alert("Erro ao listar usuarios");
        }
    };
    xhr.send();
}

function clear_list() {
    document.getElementById("lista_usuarios").innerHTML = "";
}

function fulfill_list(data) {
    let list = document.getElementById("lista_usuarios");
    for (i = 0; i < data.length; ++i) {
        var li = document.createElement('li');
        li.innerText = `Nome: ${data[i]['nome']}, Idade: ${data[i]['idade']}, CPF: ${data[i]['cpf']}`;
        list.appendChild(li);
    }
}

function main() {
    let formulario = document.getElementById("formulario");
    formulario.addEventListener("submit", async (e) => {
        e.preventDefault();
        insert(e);
      });
}


main();