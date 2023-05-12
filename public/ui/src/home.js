async function medecin(index, element) {
    let contenu = element.innerHTML;
    let json = JSON.parse(contenu);
    let doctolib = (
        await fetch("https://www.doctolib.fr/" + json["doctolib"], {
            mode: "cors",
        })
    ).body;
    console.log(doctolib);
}

function liste_medecins() {
    let medecins = $("#medecins > tbody > tr > script");
    medecins.each(medecin);
}
