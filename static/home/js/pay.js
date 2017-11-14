    /* *****************************************************************
     Conf 
     * ************************************************************** */


function myChangeFunction(){
  horas =  $("#id_hours" ).val()
  if (horas == '1'){
    $("#valor" ).text('$ 29.999')
    $('#amount').val('30000')
    $('#description').val('bolsa de 2 horas ')
    $('#referenceCode').val('was30')
    $('#buttonId').val('VgDL7MJqt+GBWo8uoFOIhaTqSLyNVHsRsuDVZWQb1ysk4Ni4w53s+A==')
    $('#signature').val('5f559e872c134fa086be94c8e524dbefb57f60fc961d7a11e3404fce248bacf2')
  }else{
    if (horas == '2') {
      $("#valor" ).text('$ 49.999')
      $('#amount').val('50000')
      $('#description').val('bolsa de 4 horas ')
      $('#referenceCode').val('was40')
      $('#buttonId').val('qU/v/bMaGiAqLXGaEOu7+cUM4R9dNDD4zlVCGynFokXyYOI6fhBmRA==')
      $('#signature').val('c5ff7887620a77eba1d330a5abe9a4d6784d356038bdbee97ad6b5e60ab153b0')   
    } else {
      if (horas == '3') {
        $("#valor" ).text('$ 89.999')
        $('#amount').val('90000')
        $('#description').val('bolsa de 8 horas ')
        $('#referenceCode').val('was80')
        $('#buttonId').val('sFoNi8jMp0L3552jKANcD8TBUIAr1xy7gooF1Q1+N2m5wgrLMVq/FQ==')
        $('#signature').val('53a45b80f815b743052dad5cb42977a60b489dcf15ddf1104834578d2a6ff3b7')   
        
      }
    }
  } 
}


function myChangeFunction2(){





horas =  $("#id_hours2" ).val()
  if (horas == '1'){
    $("#valor2" ).text('$ 29.999')
    $('#amount2').val('30000')
    $('#description2').val('bolsa de 2 horas ')
    $('#referenceCode2').val('was30')
    $('#buttonId2').val('VgDL7MJqt+GBWo8uoFOIhaTqSLyNVHsRsuDVZWQb1ysk4Ni4w53s+A==')
    $('#signature').val('5f559e872c134fa086be94c8e524dbefb57f60fc961d7a11e3404fce248bacf2')
  }else{
    if (horas == '2') {
      $("#valor2" ).text('$ 49.999')
      $('#amount2').val('50000')
      $('#description2').val('bolsa de 4 horas ')
      $('#referenceCode2').val('was40')
      $('#buttonId2').val('qU/v/bMaGiAqLXGaEOu7+cUM4R9dNDD4zlVCGynFokXyYOI6fhBmRA==')
      $('#signature2').val('c5ff7887620a77eba1d330a5abe9a4d6784d356038bdbee97ad6b5e60ab153b0')   
    } else {
      if (horas == '3') {
        $("#valor2" ).text('$ 89.999')
        $('#amount2').val('90000')
        $('#description2').val('bolsa de 8 horas ')
        $('#referenceCode2').val('was80')
        $('#buttonId2').val('sFoNi8jMp0L3552jKANcD8TBUIAr1xy7gooF1Q1+N2m5wgrLMVq/FQ==')
        $('#signature2').val('53a45b80f815b743052dad5cb42977a60b489dcf15ddf1104834578d2a6ff3b7')   
        
      }
    }
  } 
  
}