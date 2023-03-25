//copyfromシートの内容を取得→pastetoシートの最終行以降に貼り付け→copyfromシートをリセット

function reset_record() {
  var master = SpreadsheetApp.openByUrl("https://~");
  var copyfrom = master.getSheetByName("タイムカード");
  var pasteto = master.getSheetByName("アーカイブ");
  var copyfrom_lastrow = copyfrom.getLastRow(); //読み込んだシートの最終行を取得する
  var copyRange = copyfrom.getRange(2,1,copyfrom_lastrow, 7).getValues();
  var pasteto_lastrow = pasteto.getLastRow();
  pasteto.getRange(pasteto_lastrow+1, 1, copyfrom_lastrow, 7).setValues(copyRange);

  var del_range_1 = copyfrom.getRange(2,1, copyfrom_lastrow, 5);
  var del_range_2 = copyfrom.getRange(2,7, copyfrom_lastrow, 1);
  del_range_1.clear()
  del_range_2.clear()
}

// end!
