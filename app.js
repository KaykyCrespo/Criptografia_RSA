var btnEntrar = document.querySelector("#entrar")
var btnSair = document.querySelector("#sair")

var body = document.querySelector("body");

btnEntrar.addEventListener("click", function() {
    body.className = "entrar-js"
});

btnSair.addEventListener("click", function() {
    body.className = "sair-js"
});

var helpButton = document.querySelector("#helpButton");
var helpDialog = document.querySelector("#helpDialog");

helpButton.addEventListener("click", function() {
    helpDialog.showModal();
});

helpDialog.addEventListener("click", function(event) {
    if (event.target === helpDialog) {
        helpDialog.close();
    }
});

document.querySelectorAll('input[name="criptografia"], input[name="criptografia2"]').forEach(function(method) {
    method.addEventListener("click", function() {
        var notice = document.querySelector(method.name === "criptografia" ? "#methodNoticeEncrypt" : "#methodNoticeDecrypt");
        var panel = method.closest(".second-column");
        var tlsSimulation = document.querySelector(method.name === "criptografia" ? "#tlsSimulationEncrypt" : "#tlsSimulationDecrypt");
        var privateKey = document.querySelector(method.name === "criptografia" ? "#chave-privada1" : "#chave-privada2");
        var publicKey = document.querySelector(method.name === "criptografia" ? "#chave-publica1" : "#chave-publica2");
        var fieldElements = panel.querySelectorAll(".field-label, .form");

        method.checked = true;
        notice.hidden = true;
        notice.textContent = "";
        tlsSimulation.hidden = method.value !== "TLS";
        fieldElements.forEach(function(element) {
            element.hidden = method.value === "TLS";
        });

        if (method.value === "RSA" || method.value === "DES" || method.value === "TWOFISH" || method.value === "SAFER") {
            var labels = {
                RSA: ["Chave privada RSA", "Chave pública RSA"],
                DES: ["Chave DES (8 bytes hex)", "IV DES (8 bytes hex)"],
                TWOFISH: ["Chave Twofish (16 bytes hex)", "IV Twofish (16 bytes hex)"],
                SAFER: ["Chave SAFER K-64 (8 bytes hex)", "IV SAFER (8 bytes hex)"]
            };
            notice.hidden = true;
            notice.textContent = "";
            privateKey.placeholder = labels[method.value][0];
            publicKey.placeholder = labels[method.value][1];
            return;
        }

        privateKey.placeholder = "Chave privada RSA";
        publicKey.placeholder = "Chave pública RSA";
    });
});

document.querySelectorAll(".workflow-tab").forEach(function(tab) {
    tab.addEventListener("click", function() {
        var workflow = tab.dataset.workflowTarget;
        var panel = document.querySelector(workflow === "encrypt" ? "#cryptoPanel" : "#decryptPanel");

        document.body.dataset.workflow = workflow;
        document.querySelectorAll(".workflow-tab").forEach(function(workflowTab) {
            var selected = workflowTab === tab;
            workflowTab.classList.toggle("is-active", selected);
            workflowTab.setAttribute("aria-pressed", selected ? "true" : "false");
        });

        if (window.matchMedia("(max-width: 860px)").matches) {
            window.scrollTo({top: 0, behavior: "smooth"});
        }
    });
});

function avancarTls(workflow) {
    var steps = document.querySelectorAll("#tlsSteps" + (workflow === "encrypt" ? "Encrypt" : "Decrypt") + " li");
    var progress = document.querySelector("#tlsProgress" + (workflow === "encrypt" ? "Encrypt" : "Decrypt"));
    var nextButton = document.querySelector("#tlsNext" + (workflow === "encrypt" ? "Encrypt" : "Decrypt"));
    var current = Number(nextButton.dataset.current || "0");

    if (current >= steps.length - 1) {
        return;
    }

    steps[current].hidden = true;
    current += 1;
    steps[current].hidden = false;
    nextButton.dataset.current = String(current);
    progress.textContent = "Etapa " + (current + 1) + " de " + steps.length;

    if (current === steps.length - 1) {
        nextButton.disabled = true;
        nextButton.innerHTML = 'Handshake finalizado <i class="bi bi-check2" aria-hidden="true"></i>';
    }
}


function mostrarSenhaPrimary(){
    var inputPassPrimary = document.getElementById('msgCriptografada-primary')
    var btnShowPassPrimary = document.getElementById('btn-msgCriptografada-primary')

    if(inputPassPrimary.type === 'password'){
        inputPassPrimary.setAttribute('type','text')
        btnShowPassPrimary.classList.replace('bi-eye-fill','bi-eye-slash-fill')
    }else if(inputPassPrimary.type === 'text'){
        inputPassPrimary.setAttribute('type','password')
        btnShowPassPrimary.classList.replace('bi-eye-slash-fill','bi-eye-fill')
    }
}

function mostrarSenhaSecond(){
    var inputPassSecond = document.getElementById('msgDescriptografada-second')
    var btnShowPassSecond = document.getElementById('btn-msgDescriptografada-second')

    if(inputPassSecond.type === 'password'){
        inputPassSecond.setAttribute('type','text')
        btnShowPassSecond.classList.replace('bi-eye-fill','bi-eye-slash-fill')
    }else if(inputPassSecond.type === 'text'){
        inputPassSecond.setAttribute('type','password')
        btnShowPassSecond.classList.replace('bi-eye-slash-fill','bi-eye-fill')
    } 
}

function btnInfoEnterEsquerda(){
    var btnInformacoes = document.getElementById('btnInformacoesEsquerda') 
    var btnInfo = document.getElementById('informacoesEsquerdaFront')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('src','imagens/info-circle-fill.png')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('src','imagens/info-circle.png')
    } 
}

function btnInfoOutEsquerda(){
    var btnInformacoes = document.getElementById('btnInformacoesEsquerda') 
    var btnInfo = document.getElementById('informacoesEsquerdaFront')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('src','imagens/info-circle-fill.png')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('src','imagens/info-circle.png')
    } 
}

function btnInfoEnterDireita(){
    var btnInformacoes = document.getElementById('btnInformacoesDireita') 
    var btnInfo = document.getElementById('informacoesDireita')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('src','imagens/info-circle-fill.png')
    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('src','imagens/info-circle.png')
    } 
}

function btnInfoOutDireita(){
    var btnInformacoes = document.getElementById('btnInformacoesDireita') 
    var btnInfo = document.getElementById('informacoesDireita')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('src','imagens/info-circle-fill.png')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('src','imagens/info-circle.png')
    } 
}

function abrirDireita(){
    var infoimage = document.getElementById('popup')
    infoimage.style.display = 'block';
    infoimage.style.animation = 'slideInfoDireita 1.8s'
    var btninfo = document.getElementById('myRect')
    btninfo.setAttribute('fill', 'black')
    var transicaoTexto = document.getElementById('infoTextoEsquerda')
    transicaoTexto.style.animation = 'transicaoTextoEsquerda 1.8s'
}

function abrirEsquerda(){
    var infoimage = document.getElementById('popup')
    infoimage.style.display = 'block';
    infoimage.style.animation = 'slideInfoEsquerda 1.8s'
    var btninfo = document.getElementById('myRect')
    btninfo.setAttribute('fill', 'black')
    var btnInfoFront = document.getElementById('informacoesEsquerdaFront')
    btnInfoFront.style.visibility = 'hidden'
    var transicaoTexto = document.getElementById('infoTextoEsquerda')
    transicaoTexto.style.animation = 'transicaoTextoDireita 1.8s'
}

function fecharDireita(){
    var infoimage = document.getElementById('popup')
    infoimage.style.display = 'none';
    infoimage.style.animation = 'slideInfoDireita 1s'
    var btninfo = document.getElementById('myRect')
    btninfo.setAttribute('fill', 'white')
}


/*--------------------------------PROXIMA PÁGINA------------------------------*/
function proximaPagina1(){
    var btnVoltarInfo1 = document.getElementById('conteudoInfo1')
    btnVoltarInfo1.style.visibility = 'hidden'
    var btnVoltarInfoTexto1 = document.getElementById('topicosInfo1')
    btnVoltarInfoTexto1.style.visibility = 'hidden'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem1')
    btnVoltarInfoImagem2.style.visibility = 'hidden'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina1')
    btnVoltarInfoPaginacao2.style.visibility = 'hidden'


    var btnVoltarInfo2 = document.getElementById('conteudoInfo2')
    btnVoltarInfo2.style.visibility = 'visible'
    var btnVoltarInfoTexto2 = document.getElementById('topicosInfo2')
    btnVoltarInfoTexto2.style.visibility = 'visible'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem2')
    btnVoltarInfoImagem2.style.visibility = 'visible'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina2')
    btnVoltarInfoPaginacao2.style.visibility = 'visible'
}

function proximaPagina2(){
    var btnVoltarInfo1 = document.getElementById('conteudoInfo3')
    btnVoltarInfo1.style.visibility = 'visible'
    var btnVoltarTexto = document.getElementById('topicosInfo3')
    btnVoltarTexto.style.visibility = 'visible'
    var btnVoltarImagem = document.getElementById('topicoImagem3')
    btnVoltarImagem.style.visibility = 'visible'
    var btnVoltarImagem = document.getElementById('pagina3')
    btnVoltarImagem.style.visibility = 'visible'


    var btnVoltarInfo2 = document.getElementById('conteudoInfo2')
    btnVoltarInfo2.style.visibility = 'hidden'
    var btnVoltarInfoTexto2 = document.getElementById('topicosInfo2')
    btnVoltarInfoTexto2.style.visibility = 'hidden'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem2')
    btnVoltarInfoImagem2.style.visibility = 'hidden'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina2')
    btnVoltarInfoPaginacao2.style.visibility = 'hidden'
}

function proximaPagina3(){
    var btnVoltarInfo1 = document.getElementById('conteudoInfo4')
    btnVoltarInfo1.style.visibility = 'visible'
    var btnVoltarInfoTexto1 = document.getElementById('topicosInfo4')
    btnVoltarInfoTexto1.style.visibility = 'visible'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem4')
    btnVoltarInfoImagem2.style.visibility = 'visible'
    var btnVoltarInfoContorno= document.getElementById('pagina4')
    btnVoltarInfoContorno.style.visibility = 'visible'


    var btnVoltarInfo2 = document.getElementById('conteudoInfo3')
    btnVoltarInfo2.style.visibility = 'hidden'
    var btnVoltarInfoTexto2 = document.getElementById('topicosInfo3')
    btnVoltarInfoTexto2.style.visibility = 'hidden'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem3')
    btnVoltarInfoImagem2.style.visibility = 'hidden'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina3')
    btnVoltarInfoPaginacao2.style.visibility = 'hidden'
}

function proximaPagina4(){
    var btnVoltarInfo1 = document.getElementById('conteudoInfo5')
    btnVoltarInfo1.style.visibility = 'visible'
    var btnVoltarInfoTexto1 = document.getElementById('topicosInfo5')
    btnVoltarInfoTexto1.style.visibility = 'visible'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem5')
    btnVoltarInfoImagem2.style.visibility = 'visible'
    var btnVoltarInfoContorno= document.getElementById('pagina5')
    btnVoltarInfoContorno.style.visibility = 'visible'


    var btnVoltarInfo2 = document.getElementById('conteudoInfo4')
    btnVoltarInfo2.style.visibility = 'hidden'
    var btnVoltarInfoTexto2 = document.getElementById('topicosInfo4')
    btnVoltarInfoTexto2.style.visibility = 'hidden'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem4')
    btnVoltarInfoImagem2.style.visibility = 'hidden'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina4')
    btnVoltarInfoPaginacao2.style.visibility = 'hidden'
}

function proximaPagina5(){
    var btnVoltarInfo1 = document.getElementById('conteudoInfo6')
    btnVoltarInfo1.style.visibility = 'visible'
    var btnVoltarInfoTexto1 = document.getElementById('topicosInfo6')
    btnVoltarInfoTexto1.style.visibility = 'visible'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem6')
    btnVoltarInfoImagem2.style.visibility = 'visible'
    var btnVoltarInfoContorno= document.getElementById('pagina6')
    btnVoltarInfoContorno.style.visibility = 'visible'


    var btnVoltarInfo2 = document.getElementById('conteudoInfo5')
    btnVoltarInfo2.style.visibility = 'hidden'
    var btnVoltarInfoTexto2 = document.getElementById('topicosInfo5')
    btnVoltarInfoTexto2.style.visibility = 'hidden'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem5')
    btnVoltarInfoImagem2.style.visibility = 'hidden'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina5')
    btnVoltarInfoPaginacao2.style.visibility = 'hidden'
}

function proximaPagina6(){
    var btnVoltarInfo1 = document.getElementById('conteudoInfo7')
    btnVoltarInfo1.style.visibility = 'visible'
    var btnVoltarInfoTexto1 = document.getElementById('topicosInfo7')
    btnVoltarInfoTexto1.style.visibility = 'visible'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem7')
    btnVoltarInfoImagem2.style.visibility = 'visible'
    var btnVoltarInfoContorno= document.getElementById('pagina7')
    btnVoltarInfoContorno.style.visibility = 'visible'


    var btnVoltarInfo2 = document.getElementById('conteudoInfo6')
    btnVoltarInfo2.style.visibility = 'hidden'
    var btnVoltarInfoTexto2 = document.getElementById('topicosInfo6')
    btnVoltarInfoTexto2.style.visibility = 'hidden'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem6')
    btnVoltarInfoImagem2.style.visibility = 'hidden'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina6')
    btnVoltarInfoPaginacao2.style.visibility = 'hidden'
}

function proximaPagina7(){
    var btnVoltarInfo1 = document.getElementById('conteudoInfo8')
    btnVoltarInfo1.style.visibility = 'visible'
    var btnVoltarInfoTexto1 = document.getElementById('topicosInfo8')
    btnVoltarInfoTexto1.style.visibility = 'visible'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem8')
    btnVoltarInfoImagem2.style.visibility = 'visible'
    var btnVoltarInfoContorno= document.getElementById('pagina8')
    btnVoltarInfoContorno.style.visibility = 'visible'


    var btnVoltarInfo2 = document.getElementById('conteudoInfo7')
    btnVoltarInfo2.style.visibility = 'hidden'
    var btnVoltarInfoTexto2 = document.getElementById('topicosInfo7')
    btnVoltarInfoTexto2.style.visibility = 'hidden'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem7')
    btnVoltarInfoImagem2.style.visibility = 'hidden'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina7')
    btnVoltarInfoPaginacao2.style.visibility = 'hidden'
}

function proximaPagina8(){
    var btnVoltarInfo1 = document.getElementById('conteudoInfo9')
    btnVoltarInfo1.style.visibility = 'visible'
    var btnVoltarInfoTexto1 = document.getElementById('topicosInfo9')
    btnVoltarInfoTexto1.style.visibility = 'visible'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem9')
    btnVoltarInfoImagem2.style.visibility = 'visible'
    var btnVoltarInfoContorno= document.getElementById('pagina9')
    btnVoltarInfoContorno.style.visibility = 'visible'


    var btnVoltarInfo2 = document.getElementById('conteudoInfo8')
    btnVoltarInfo2.style.visibility = 'hidden'
    var btnVoltarInfoTexto2 = document.getElementById('topicosInfo8')
    btnVoltarInfoTexto2.style.visibility = 'hidden'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem8')
    btnVoltarInfoImagem2.style.visibility = 'hidden'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina8')
    btnVoltarInfoPaginacao2.style.visibility = 'hidden'
}

function proximaPagina9(){
    var btnVoltarInfo1 = document.getElementById('conteudoInfo10')
    btnVoltarInfo1.style.visibility = 'visible'
    var btnVoltarInfoTexto1 = document.getElementById('topicosInfo10')
    btnVoltarInfoTexto1.style.visibility = 'visible'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem10')
    btnVoltarInfoImagem2.style.visibility = 'visible'
    var btnVoltarInfoContorno= document.getElementById('pagina10')
    btnVoltarInfoContorno.style.visibility = 'visible'


    var btnVoltarInfo2 = document.getElementById('conteudoInfo9')
    btnVoltarInfo2.style.visibility = 'hidden'
    var btnVoltarInfoTexto2 = document.getElementById('topicosInfo9')
    btnVoltarInfoTexto2.style.visibility = 'hidden'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem9')
    btnVoltarInfoImagem2.style.visibility = 'hidden'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina9')
    btnVoltarInfoPaginacao2.style.visibility = 'hidden'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina8')
    btnVoltarInfoPaginacao2.style.visibility = 'hidden'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem8')
    btnVoltarInfoImagem2.style.visibility = 'hidden'
}


/*------------------------------PAGINA ANTERIOR--------------------------*/
function paginaAnterior2(){
    var btnVoltarInfo1 = document.getElementById('conteudoInfo1')
    btnVoltarInfo1.style.visibility = 'visible'
    var btnVoltarInfoTexto1 = document.getElementById('topicosInfo1')
    btnVoltarInfoTexto1.style.visibility = 'visible'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem1')
    btnVoltarInfoImagem2.style.visibility = 'visible'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina1')
    btnVoltarInfoPaginacao2.style.visibility = 'visible'


    var btnVoltarInfo2 = document.getElementById('conteudoInfo2')
    btnVoltarInfo2.style.visibility = 'hidden'
    var btnVoltarInfoTexto2 = document.getElementById('topicosInfo2')
    btnVoltarInfoTexto2.style.visibility = 'hidden'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem2')
    btnVoltarInfoImagem2.style.visibility = 'hidden'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina2')
    btnVoltarInfoPaginacao2.style.visibility = 'hidden'
}

function paginaAnterior3(){
    var btnVoltarInfo1 = document.getElementById('conteudoInfo2')
    btnVoltarInfo1.style.visibility = 'visible'
    var btnVoltarInfoTexto1 = document.getElementById('topicosInfo2')
    btnVoltarInfoTexto1.style.visibility = 'visible'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem2')
    btnVoltarInfoImagem2.style.visibility = 'visible'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina2')
    btnVoltarInfoPaginacao2.style.visibility = 'visible'


    var btnVoltarInfo2 = document.getElementById('conteudoInfo3')
    btnVoltarInfo2.style.visibility = 'hidden'
    var btnVoltarInfoTexto2 = document.getElementById('topicosInfo3')
    btnVoltarInfoTexto2.style.visibility = 'hidden'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem3')
    btnVoltarInfoImagem2.style.visibility = 'hidden'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina3')
    btnVoltarInfoPaginacao2.style.visibility = 'hidden'
}

function paginaAnterior4(){
    var btnVoltarInfo1 = document.getElementById('conteudoInfo3')
    btnVoltarInfo1.style.visibility = 'visible'
    var btnVoltarInfoTexto1 = document.getElementById('topicosInfo3')
    btnVoltarInfoTexto1.style.visibility = 'visible'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem3')
    btnVoltarInfoImagem2.style.visibility = 'visible'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina3')
    btnVoltarInfoPaginacao2.style.visibility = 'visible'


    var btnVoltarInfo2 = document.getElementById('conteudoInfo4')
    btnVoltarInfo2.style.visibility = 'hidden'
    var btnVoltarInfoTexto2 = document.getElementById('topicosInfo4')
    btnVoltarInfoTexto2.style.visibility = 'hidden'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem4')
    btnVoltarInfoImagem2.style.visibility = 'hidden'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina4')
    btnVoltarInfoPaginacao2.style.visibility = 'hidden'
}

function paginaAnterior5(){
    var btnVoltarInfo1 = document.getElementById('conteudoInfo4')
    btnVoltarInfo1.style.visibility = 'visible'
    var btnVoltarInfoTexto1 = document.getElementById('topicosInfo4')
    btnVoltarInfoTexto1.style.visibility = 'visible'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem4')
    btnVoltarInfoImagem2.style.visibility = 'visible'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina4')
    btnVoltarInfoPaginacao2.style.visibility = 'visible'


    var btnVoltarInfo2 = document.getElementById('conteudoInfo5')
    btnVoltarInfo2.style.visibility = 'hidden'
    var btnVoltarInfoTexto2 = document.getElementById('topicosInfo5')
    btnVoltarInfoTexto2.style.visibility = 'hidden'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem5')
    btnVoltarInfoImagem2.style.visibility = 'hidden'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina5')
    btnVoltarInfoPaginacao2.style.visibility = 'hidden'
}

function paginaAnterior6(){
    var btnVoltarInfo1 = document.getElementById('conteudoInfo5')
    btnVoltarInfo1.style.visibility = 'visible'
    var btnVoltarInfoTexto1 = document.getElementById('topicosInfo5')
    btnVoltarInfoTexto1.style.visibility = 'visible'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem5')
    btnVoltarInfoImagem2.style.visibility = 'visible'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina5')
    btnVoltarInfoPaginacao2.style.visibility = 'visible'


    var btnVoltarInfo2 = document.getElementById('conteudoInfo6')
    btnVoltarInfo2.style.visibility = 'hidden'
    var btnVoltarInfoTexto2 = document.getElementById('topicosInfo6')
    btnVoltarInfoTexto2.style.visibility = 'hidden'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem6')
    btnVoltarInfoImagem2.style.visibility = 'hidden'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina6')
    btnVoltarInfoPaginacao2.style.visibility = 'hidden'
}

function paginaAnterior7(){
    var btnVoltarInfo1 = document.getElementById('conteudoInfo6')
    btnVoltarInfo1.style.visibility = 'visible'
    var btnVoltarInfoTexto1 = document.getElementById('topicosInfo6')
    btnVoltarInfoTexto1.style.visibility = 'visible'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem6')
    btnVoltarInfoImagem2.style.visibility = 'visible'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina6')
    btnVoltarInfoPaginacao2.style.visibility = 'visible'


    var btnVoltarInfo2 = document.getElementById('conteudoInfo7')
    btnVoltarInfo2.style.visibility = 'hidden'
    var btnVoltarInfoTexto2 = document.getElementById('topicosInfo7')
    btnVoltarInfoTexto2.style.visibility = 'hidden'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem7')
    btnVoltarInfoImagem2.style.visibility = 'hidden'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina7')
    btnVoltarInfoPaginacao2.style.visibility = 'hidden'
}

function paginaAnterior8(){
    var btnVoltarInfo1 = document.getElementById('conteudoInfo7')
    btnVoltarInfo1.style.visibility = 'visible'
    var btnVoltarInfoTexto1 = document.getElementById('topicosInfo7')
    btnVoltarInfoTexto1.style.visibility = 'visible'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem7')
    btnVoltarInfoImagem2.style.visibility = 'visible'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina7')
    btnVoltarInfoPaginacao2.style.visibility = 'visible'


    var btnVoltarInfo2 = document.getElementById('conteudoInfo8')
    btnVoltarInfo2.style.visibility = 'hidden'
    var btnVoltarInfoTexto2 = document.getElementById('topicosInfo8')
    btnVoltarInfoTexto2.style.visibility = 'hidden'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem8')
    btnVoltarInfoImagem2.style.visibility = 'hidden'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina8')
    btnVoltarInfoPaginacao2.style.visibility = 'hidden'
}

function paginaAnterior9(){
    var btnVoltarInfo1 = document.getElementById('conteudoInfo8')
    btnVoltarInfo1.style.visibility = 'visible'
    var btnVoltarInfoTexto1 = document.getElementById('topicosInfo8')
    btnVoltarInfoTexto1.style.visibility = 'visible'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem8')
    btnVoltarInfoImagem2.style.visibility = 'visible'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina8')
    btnVoltarInfoPaginacao2.style.visibility = 'visible'


    var btnVoltarInfo2 = document.getElementById('conteudoInfo9')
    btnVoltarInfo2.style.visibility = 'hidden'
    var btnVoltarInfoTexto2 = document.getElementById('topicosInfo9')
    btnVoltarInfoTexto2.style.visibility = 'hidden'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem9')
    btnVoltarInfoImagem2.style.visibility = 'hidden'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina9')
    btnVoltarInfoPaginacao2.style.visibility = 'hidden'
}

function paginaAnterior10(){
    var btnVoltarInfo1 = document.getElementById('conteudoInfo9')
    btnVoltarInfo1.style.visibility = 'visible'
    var btnVoltarInfoTexto1 = document.getElementById('topicosInfo9')
    btnVoltarInfoTexto1.style.visibility = 'visible'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem9')
    btnVoltarInfoImagem2.style.visibility = 'visible'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina9')
    btnVoltarInfoPaginacao2.style.visibility = 'visible'


    var btnVoltarInfo2 = document.getElementById('conteudoInfo10')
    btnVoltarInfo2.style.visibility = 'hidden'
    var btnVoltarInfoTexto2 = document.getElementById('topicosInfo10')
    btnVoltarInfoTexto2.style.visibility = 'hidden'
    var btnVoltarInfoImagem2 = document.getElementById('topicoImagem10')
    btnVoltarInfoImagem2.style.visibility = 'hidden'
    var btnVoltarInfoPaginacao2 = document.getElementById('pagina10')
    btnVoltarInfoPaginacao2.style.visibility = 'hidden'
}

/*                MUDAR COR BOTAO -- DIREITA           */
function mudarCorBotaoPaginaProxima1(){
    var btnInformacoes = document.getElementById('botaoVoltar') 
    var btnInfo = document.getElementById('informacoesEsquerdaBackVoltar')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('fill','black')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('fill','white')
    } 
}

function mudarCorBotaoPaginaProxima2(){
    var btnInformacoes = document.getElementById('botaoVoltar2') 
    var btnInfo = document.getElementById('informacoesEsquerdaBackVoltar2')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('fill','black')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('fill','white')
    } 
}

function mudarCorBotaoPaginaProxima3(){
    var btnInformacoes = document.getElementById('botaoVoltar3') 
    var btnInfo = document.getElementById('informacoesEsquerdaBackVoltarPaginaAnterior3')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('fill','black')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('fill','white')
    } 
}

function mudarCorBotaoPaginaProxima4(){
    var btnInformacoes = document.getElementById('botaoVoltar4') 
    var btnInfo = document.getElementById('informacoesEsquerdaBackVoltarPaginaAnterior4')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('fill','black')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('fill','white')
    } 
}

function mudarCorBotaoPaginaProxima5(){
    var btnInformacoes = document.getElementById('botaoVoltar5') 
    var btnInfo = document.getElementById('informacoesEsquerdaBackVoltarPaginaAnterior5')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('fill','black')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('fill','white')
    } 
}

function mudarCorBotaoPaginaProxima6(){
    var btnInformacoes = document.getElementById('botaoVoltar6') 
    var btnInfo = document.getElementById('informacoesEsquerdaBackVoltarPaginaAnterior6')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('fill','black')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('fill','white')
    } 
}

function mudarCorBotaoPaginaProxima7(){
    var btnInformacoes = document.getElementById('botaoVoltar7') 
    var btnInfo = document.getElementById('informacoesEsquerdaBackVoltarPaginaAnterior7')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('fill','black')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('fill','white')
    } 
}

function mudarCorBotaoPaginaProxima8(){
    var btnInformacoes = document.getElementById('botaoVoltar8') 
    var btnInfo = document.getElementById('informacoesEsquerdaBackVoltarPaginaAnterior8')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('fill','black')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('fill','white')
    } 
}

function mudarCorBotaoPaginaProxima9(){
    var btnInformacoes = document.getElementById('botaoVoltar9') 
    var btnInfo = document.getElementById('informacoesEsquerdaBackVoltarPaginaAnterior9')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('fill','black')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('fill','white')
    } 
}

function mudarCorBotaoPaginaProxima10(){
    var btnInformacoes = document.getElementById('botaoVoltar10') 
    var btnInfo = document.getElementById('informacoesEsquerdaBackVoltarPaginaAnterior10')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('fill','black')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('fill','white')
    } 
}


/*                MUDAR COR BOTAO -- ESQUERDA           */
function mudarCorBotaoPaginaAnterior2(){
    var btnInformacoes = document.getElementById('botaoVoltarPaginaAnterior2') 
    var btnInfo = document.getElementById('informacoesEsquerdaBackVoltarPaginaAnterior2')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('fill','black')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('fill','white')
    } 
}

function mudarCorBotaoPaginaAnterior3(){
    var btnInformacoes = document.getElementById('botaoVoltarPaginaAnterior3') 
    var btnInfo = document.getElementById('informacoesEsquerdaBackVoltarPaginaAnterior3')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('fill','black')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('fill','white')
    } 
}

function mudarCorBotaoPaginaAnterior4(){
    var btnInformacoes = document.getElementById('botaoVoltarPaginaAnterior4') 
    var btnInfo = document.getElementById('informacoesEsquerdaBackVoltarPaginaAnterior4')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('fill','black')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('fill','white')
    } 
}

function mudarCorBotaoPaginaAnterior5(){
    var btnInformacoes = document.getElementById('botaoVoltarPaginaAnterior5') 
    var btnInfo = document.getElementById('informacoesEsquerdaBackVoltarPaginaAnterior5')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('fill','black')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('fill','white')
    } 
}

function mudarCorBotaoPaginaAnterior6(){
    var btnInformacoes = document.getElementById('botaoVoltarPaginaAnterior6') 
    var btnInfo = document.getElementById('informacoesEsquerdaBackVoltarPaginaAnterior6')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('fill','black')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('fill','white')
    } 
}

function mudarCorBotaoPaginaAnterior7(){
    var btnInformacoes = document.getElementById('botaoVoltarPaginaAnterior7') 
    var btnInfo = document.getElementById('informacoesEsquerdaBackVoltarPaginaAnterior7')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('fill','black')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('fill','white')
    } 
}

function mudarCorBotaoPaginaAnterior8(){
    var btnInformacoes = document.getElementById('botaoVoltarPaginaAnterior8') 
    var btnInfo = document.getElementById('informacoesEsquerdaBackVoltarPaginaAnterior8')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('fill','black')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('fill','white')
    } 
}

function mudarCorBotaoPaginaAnterior9(){
    var btnInformacoes = document.getElementById('botaoVoltarPaginaAnterior9') 
    var btnInfo = document.getElementById('informacoesEsquerdaBackVoltarPaginaAnterior9')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('fill','black')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('fill','white')
    } 
}

function mudarCorBotaoPaginaAnterior10(){
    var btnInformacoes = document.getElementById('botaoVoltarPaginaAnterior10') 
    var btnInfo = document.getElementById('informacoesEsquerdaBackVoltarPaginaAnterior10')

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.setAttribute('fill','black')

    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.setAttribute('fill','white')
    } 
}