var total = 0;

for (var i = 0; creditoTable.rows[i]; i++) {
    total += parseFloat(creditoTable.rows[i].cells[4].innerHTML);
}
document.write(total)