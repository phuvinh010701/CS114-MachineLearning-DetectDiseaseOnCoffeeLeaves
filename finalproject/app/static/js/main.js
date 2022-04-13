function readPath(event){
        var src = URL.createObjectURL(event.target.files[0]);
        var preview = document.getElementById("input");
        preview.src = src;
        // preview.style.setProperty("width","500","important");
        // preview.style.setProperty("height","500","important");
    }
    function sendImage(){
        var img = document.getElementById("img").files[0];
        var ajax = new XMLHttpRequest();

        var form_data = new FormData();
        form_data.append('file', document.querySelector('#img').files[0]);
        
        ajax.onreadystatechange = function(){
            if(this.status == 200 && this.readyState == 4){
                console.log(typeof(this.responseText));
                console.log(this.responseText);
                var res_json = JSON.parse(this.responseText);
                var tb = "";
                var tmp = [];
                for(var v in res_json){
                    if(v == "path"){
                        break;
                    }
                    if( tmp.includes(v) == false){
                        tmp.push(v);
                        tb =  tb  + `<tr>
                            <td>${v}</td>
                            <td>${res_json[v]["name"]}</td>
                            <td><image with="300" height="200" src=${res_json[v]["image"]}/></td>
                            <td>${res_json[v]["treatment"][0]}</td>
                            <td>${res_json[v]["guide"]}</td>
                        </tr>`;
                        console.log(res_json[v]["image"]);
                    }
                }
                console.log(tb);
                var tab = `
                <table class="table">
                <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">Tên loại bệnh</th>
                      <th scope ="col">Hình thuốc</th>
                      <th scope="col">Tên thuốc</th>
                      <th scope="col">Cách dùng</th>
                    </tr>
                      </thead>
                      <tbody>
                        ${tb}
                      </tbody>
                </tabel>`;
                // console.log(tabel);
                document.getElementById("table").innerHTML = tab;
                document.getElementById("output").src = res_json["path"];
            }
        }
        ajax.open("post","detect",true);
        // ajax.responseType="blob";
        ajax.send(form_data);
    }