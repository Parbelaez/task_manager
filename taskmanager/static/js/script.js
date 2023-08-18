document.addEventListener('DOMContentLoaded', function () {
    // Initialize sidenav
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // datepicker initialization
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
      format: 'yyyy-mm-dd',
      i18n: { done: 'Select' }
    });

    // select initialization
    let select = document.querySelectorAll('select');
    M.FormSelect.init(select);
  });