let lastSortedColumn = -1;
let lastSortDirection = 1;

function sortTable(columnIndex) {
    const table = document.querySelector('table');
    const tbody = table.tBodies[0];
    const headers = table.querySelectorAll('th');
    const rows = Array.from(tbody.rows);
    
    const isNumeric = columnIndex === 0 || columnIndex === 2;
    
    const sortDirection = (lastSortedColumn === columnIndex) 
        ? lastSortDirection * -1 
        : 1;
    
    headers.forEach(header => {
        const text = header.textContent;
        header.textContent = text.replace(/[▲▼]/g, '').trim();
    });
    
    headers[columnIndex].textContent += sortDirection === 1 ? ' ▲' : ' ▼';
    
    rows.sort((a, b) => {
        const aVal = a.cells[columnIndex].textContent;
        const bVal = b.cells[columnIndex].textContent;
        
        if (isNumeric) {
            return (parseFloat(aVal) - parseFloat(bVal)) * sortDirection;
        }
        return aVal.localeCompare(bVal) * sortDirection;
    });
    
    tbody.innerHTML = '';
    rows.forEach(row => tbody.appendChild(row));
    
    lastSortedColumn = columnIndex;
    lastSortDirection = sortDirection;
}