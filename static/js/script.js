// * Calcola il modificatore

$('.stat').bind('input', function () {
  let inputName = $(this).attr('name');
  let mod = parseInt($(this).val()) - 10;

  if (mod % 2 == 0) mod = mod / 2;
  else mod = (mod - 1) / 2;
  let modProf = mod + 2;
  modProf = '+' + modProf;
  if (isNaN(mod)) mod = '';
  else if (mod >= 0) mod = '+' + mod;

  let scoreName = inputName.slice(0, inputName.indexOf('score'));
  let modName = scoreName + 'mod';
  let saveName = scoreName + '-save';
  let saveProfName = scoreName + '-save-prof';

  $("[name='" + modName + "']").val(mod);
  $("[name='" + saveName + "']").val(mod);

  $("[name='" + saveProfName + "']").click(function () {
    if ($(this).is(':checked')) {
      $("[name='" + saveName + "']").val(modProf);
    } else if ($(this).is(':not(:checked)')) {
      $("[name='" + saveName + "']").val(mod);
    }
  });
});

// ! Non so cosa siano ste funzioni
$('.statmod').bind('change', function () {
  var name = $(this).attr('name');
  name = 'uses' + name.slice(0, name.indexOf('mod'));
});

$("[name='classlevel']").bind('input', function () {
  var classes = $(this).val();
  var r = new RegExp(/\d+/g);
  var total = 0;
  var result;
  while ((result = r.exec(classes)) != null) {
    var lvl = parseInt(result);
    if (!isNaN(lvl)) total += lvl;
  }
  var prof = 2;
  if (total > 0) {
    total -= 1;
    prof += Math.trunc(total / 4);
    prof = '+' + prof;
  } else {
    prof = '';
  }
  $("[name='proficiencybonus']").val(prof);
});

$('textarea').autoResize();