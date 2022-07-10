let choice = 0;
let choiceList = Array();

function validate(identifier) {

    if (choice !== 0) {
        let conf = confirm("Valider la sélection ?")
        if (conf) {
            let qRadix = identifier + "-";
            let question = parseInt(identifier.substring(1, 3));
            for (let i = 1; i <= 4; i++) {
                if (i !== choice) {
                    // TODO: change note style but class
                    document.getElementById(qRadix + i.toString().padStart(2, '0') + 'l').style['color'] = 'lightgray';
                }
            }
            document.getElementById(identifier).remove();
            choiceList[question] = choice
            choice = 0;
        }
    }
}


function submitMCQ2(identifier) {
    let element = document.getElementById(identifier);
    let parent = element.parentElement;
    let newBtn = document.createElement("button");
    newBtn.innerHTML = "Confirmer";
    const list = newBtn.classList;
    list.add("btn-warning", "rounded-3", "px-5", "py-3", "display-6", "shadow-lg");
    newBtn.onclick = submitMCQ;
    newBtn.onchange = submitMCQ3;
    newBtn.id = "validation";
    parent.replaceChild(newBtn, element);

}

function submitMCQ3() {
    let element = document.getElementById("validation");
    let parent = element.parentElement;
    parent.removeChild(element);
}


function submitMCQ() {
    alert("Réponses : " + JSON.stringify(choiceList));
    // let answers = {};
    // for (let i = 0; i < choiceList.length; i++) {
    //     let index = 'q'+i.toString().padStart(2,'0');
    //     if (choiceList[i])
    //         answers[index] = choiceList[i];
    //     else
    //         choiceList[index] = 'no answer';
    // }
    // alert(answers);
}
