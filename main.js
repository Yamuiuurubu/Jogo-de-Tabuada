const numeros = [2,3,4,5,6,7,8,9]

const respostaInput = document.getElementById("resposta")
const perguntaElement = document.getElementById("pergunta")
const mensagem = document.getElementById("mensagem")

var x1,x2

function gerar() {
    i1 = Math.floor(Math.random() * numeros.length)
    i2 = Math.floor(Math.random() * numeros.length)

    x1 = numeros[i1]
    x2 = numeros[i2]

    perguntaElement.textContent = `Quanto é ${x1} x ${x2}?`
}

function enviar() {
    var resposta_certa = x1*x2
    var resposta = respostaInput.value

    if(resposta == resposta_certa) {
        respostaInput.value = ''
        respostaInput.focus()
        return gerar()
    } else {
        console.log("errou")
        respostaInput.value = ''
    }
}

gerar()