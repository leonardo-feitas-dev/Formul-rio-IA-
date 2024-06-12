
function applyFilter() {
    const plano = document.getElementById('plano').value;
    const categoria = document.getElementById('categoria').value;
    let url = '/modelos';
    if (plano || categoria) {
        url += '?';
        if (plano) {
            url += `plano=${plano}`;
        }
        if (categoria) {
            if (plano) {
                url += '&';
            }
            url += `categoria=${categoria}`;
        }
    }
    window.location.href = url;
}
