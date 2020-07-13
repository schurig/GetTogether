import $ from 'jquery'
import 'select2'

function formatResult(result) {
  return result.display;
}

function formatResultSelection(result) {
  return result.display;
}

$(document).ready(function () {
  $('#id_category').select2();
  $('#id_tz').select2();
  $("#city_select").select2({
    minimumInputLength: 3,
    placeholder: 'Search for a city',
    ajax: {
      url: '/api/cities/?q=',
      dataType: 'json',
      cache: true,
      processResults: function (data) {
        return {
          results: data
        };
      }
    },
    templateResult: formatResult,
    templateSelection: formatResultSelection
  }).on('select2:select', function (e) {
    var data = e.params.data;
    $("#id_tz").val(data.tz).trigger('change');
  });

  // $("#city_select").lookup({
  //   search: function (searchText, callback) {
  //     if (searchText.length < 3) return callback(searchText, []);
  //     $.getJSON("/api/cities/?q=" + searchText, function (data) {
  //       var m = this.url.match(/q=([^&]+)/);
  //       var q = "";
  //       if (m && m.length > 0) {
  //         q = this.url.match(/q=([^&]+)/)[1]
  //       }

  //       return callback(q, data);
  //     });
  //   },
  //   select: function (event, ui) {
  //     $("#id_tz").val(ui.data.tz);
  //     $("#id_tz").selectmenu("refresh");
  //   }
  // })
});