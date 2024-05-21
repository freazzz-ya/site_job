document.querySelectorAll('.table-btn-2').forEach(btn => {
  btn.addEventListener('click', function() {
    let target = this.getAttribute('data-target');
    let tables = document.querySelectorAll('.table');
    tables.forEach(table => {
      if (table.id === target) {
        table.style.display = 'block';
      } else {
        table.style.display = 'none';
      }
    });
    document.querySelectorAll('.table-btn-2').forEach(btn => {
      btn.classList.remove('active-btn-2');
    });
    this.classList.add('active-btn-2');
  });
});