let getTds = document.querySelectorAll('table tr')

getTds.forEach(function (row) {
    let tr = row.querySelectorAll('td')
    let key = 0
    tr.forEach(function (td) {
        if (td.textContent == 'отменена') {
            key = 1
        }
        if (td.textContent == 'в работе') {
            key = 2
        }
        if (td.textContent == 'выполнен') {
            key = 3
        }
    })
    if (key == 1) {
        row.style.background = 'rgba(158, 0, 0, 0.2)'
    } else if (key == 2) {
        row.style.background = 'rgba(255, 217, 4, 0.2)'
    } else if (key == 3) {
        row.style.background = 'rgba(55, 247, 62, 0.2)'
    }
})