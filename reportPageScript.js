var tableDivElement = document.getElementById("table_div");
var sortSelect = document.getElementById("sort_select");
var filterField = document.getElementById("filter_text");
var filterDropdown = document.getElementById("filter_dropdown");
var filterRadio = document.getElementsByName("filter_radio");
var filterDropdown = document.getElementById("filter_dropdown");
var filterSortBttn = document.getElementById("filter_sort_bttn");
var resetBttn = document.getElementById("reset_bttn");
var sem1Bar = document.getElementById("sem1Bar");
var sem2Bar = document.getElementById("sem2Bar");
var analyticsSummary = document.getElementById("analytics_summary");
var tableData = [];
var tempTableData = [];
var tableHeadder = [];
var fullTable = [];
var sortParameter = null;
var filterParameter = null;
var filterParameter2 = null;
var filterParameter3 = null;





csvToArray();
createTable(fullTable);
updateChart();
displayTable();





function csvToArray() {
    
    var record = tableDivElement.innerText.split("*");

    for (var i =0; i < record.length; i++) {
        var recordArr = record[i].split(",");
        tableData.push(recordArr);
    }
       
    tableData.pop(); //removes empty array
    tableHeadder = tableData.shift(); //creates a table headder only array
    tempTableData = tableData.slice();
    createFullTable();
}






function createTable(fullTable) {

    var rowCount = 0;
    var table = document.createElement('table');
    var tableBody = document.createElement('tbody');
  
    fullTable.forEach(function(rowData) {
      var row = document.createElement('tr');
  
      rowData.forEach(function(cellData) {
        if (rowCount == 0) {
            var cell = document.createElement('th');
        }
        else {
            var cell = document.createElement('td');
        }
        cell.appendChild(document.createTextNode(cellData));
        row.appendChild(cell);
      });
  
      tableBody.appendChild(row);
      rowCount++;
    });
  
    table.appendChild(tableBody);
    tableDivElement.innerHTML = "";
    tableDivElement.appendChild(table);
  }






  function displayTable() {
    tableDivElement.style.display = "table";
  }






  function createFullTable() {
    var tempData = [];
    var tempHeadder = [];

    tempData = tempTableData.slice();
    tempHeadder = tableHeadder.slice();
    tempData.unshift(tempHeadder);
    fullTable = tempData;
  }






  function filterSort(){
    if (parseFloat(filterField.value) > 0) { //validates field input
      filterParameter = filterField.value;
    }
    else{
      alert("Filter must be a number greater than zero");
      return;
    }

    sortParameter = sortSelect.value;

    filterParameter2 = filterDropdown.value;

    for (var i = 0; i < filterRadio.length; i++){
      if (filterRadio[i].checked){
        filterParameter3 = i;
      }
    }

    tempTableData = sortData(tableData, 0, (tableData.length-1), filterParameter2) //sort data according to filter 
    tempTableData = filterData(tempTableData, filterParameter, filterParameter2, filterParameter3);
    tempTableData = sortData(tempTableData, 0, (tempTableData.length-1), sortParameter); //final sort according to sort input
    createFullTable();
    createTable(fullTable);
    updateChart()

    document.getElementById('sort_select').selectedIndex = 0;
    document.getElementById('filter_text').value = '';
    document.getElementById('filter_dropdown').selectedIndex = 0;
    document.getElementById('filter_greater').checked = true;
  }




  function reset() {

    tempTableData = tableData.slice()
    createFullTable();
    createTable(fullTable);
    updateChart()

    document.getElementById('sort_select').selectedIndex = 0;
    document.getElementById('filter_text').value = '';
    document.getElementById('filter_dropdown').selectedIndex = 0;
    document.getElementById('filter_greater').checked = true;
  }





// Merge sort algorithm, l left index, r right index
function sortData(arr,l, r, sortArg){
  if(l>=r){
      return arr;
  }
  var m =l+ parseInt((r-l)/2);
  sortData(arr, l, m, sortArg);
  sortData(arr, m+1, r, sortArg);
  merge(arr, l, m, r, sortArg);
  return arr;
}






  function merge(arr, l, m, r, sortArg){
    var n1 = m - l + 1;
    var n2 = r - m;
 
    // Create temp arrays
    var L = new Array(n1); 
    var R = new Array(n2);
 
    // Copy data to temp arrays L[] and R[]
    for (var i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (var j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];
 
    var i = 0; // Initial index of first subarray
    var j = 0; // Initial index of second subarray
    var k = l; // Initial index of merged subarray
 
    while (i < n1 && j < n2) {
        if (L[i][sortArg] <= R[j][sortArg]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
 
    // Copy the remaining elements of L[], if there are any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
 
    // Copy the remaining elements of R[], if there are any
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}







function filterData(arr, target, field, direction) {
    target = parseFloat(target);
    let n = arr.length;
    let tempList = [];
 
    // Corner cases
    if (target < parseFloat(arr[0][field])) 
      return filterCases(arr, target, 0, field, direction, 0);
    if (target > arr[n - 1][field])
      return filterCases(arr, target, n-1, field, direction, 0);
 
    // Doing binary search 
    let l = 0, r = n, mid = 0;
    while (l < r) {
        mid = Math.floor((l + r) / 2);
      
        if (arr[mid][field] == target)
            return filterCases(arr, target, mid, field, direction, 1);
 
        // If target is less than array element,then search in left 
        if (target < arr[mid][field]){
      
            // If target is greater than previous to mid, return closest of two
            if (mid > 0 && target > arr[mid - 1][field]) 
                return getClosest(arr[mid - 1], arr[mid], target, (mid - 1), mid, arr, field, direction);

            r = mid; // Repeat for left half             
        }
 
        else // If target is greater than mid
        {
            if (mid < n - 1 && target < arr[mid + 1][field]) 
                return getClosest(arr[mid], arr[mid + 1], target, mid, (mid - 1), arr, field, direction);                
            l = mid + 1; // update i
        }
    }
    // Only single element left after search
    tempList = filterCases(arr, target, mid, field, direction, 0);

    return tempList;
}






function getClosest(val1, val2, target, index1, index2, arr, field, direction){
    if (target - val1[field] >= val2[field] - target) {
        return filterCases(arr, target, index2, field, direction); 
    }       
    else{
        return filterCases(arr, target, index1, field, direction); 
    }       
}






function filterCases(arr, target, index, field, direction, inList) {
  let tempList = [];

  if (parseFloat(arr[index][field]) == target && direction == 0) {//copy all elements above (inclusive)
    tempList = arr.slice(index, arr.length);
  }
  if (parseFloat(arr[index][field]) == target && direction == 1) {//copy all elements below (inclusive)
    tempList = arr.slice(0, index+1);
  }
  if (parseFloat(arr[index][field]) > target && direction == 0) {//copy all elements above target
    tempList = arr.slice(index, arr.length);
  }
  if (parseFloat(arr[index][field]) > target && direction == 1) {//copy all elements below mid
    tempList = arr.slice(0, index-1); 
  }
  if (parseFloat(arr[index][field]) < target && direction == 0) {//copy all elements above
    tempList = arr.slice(index+1, arr.length); 
  }
  if (parseFloat(arr[index][field]) < target && direction == 1) {//copy all elements below 
    tempList = arr.slice(0, index); 
  }
  if (parseFloat(arr[index][field]) > target && direction == 0 && inList == 0) {//return all elements
    tempList = arr.slice();  
  }
  if (parseFloat(arr[index][field]) > target && direction == 1 && inList == 0) {//no elements
    tempList = [["","","","",""],["","","","",""]]; 
  }
  if (parseFloat(arr[index][field]) < target && direction == 0 && inList == 0) {//no elements
    tempList = [["","","","",""],["","","","",""]];  
  }
  if (parseFloat(arr[index][field]) < target && direction == 1 && inList == 0) {//return all elements
    tempList = arr.slice();; 
  }

  return tempList;
}





function updateChart() {
  
let sem1Sum = 0;
let sem2Sum = 0;
let sem1Avg = 0;
let sem2Avg = 0;
let sem1Percentage = 0;
let sem2Percentage = 0;

  for (let i=0; i<tempTableData.length; i++) {
    sem1Sum = sem1Sum + parseFloat(tempTableData[i][2]);
    sem2Sum = sem2Sum + parseFloat(tempTableData[i][3]);
  }

  sem1Avg = (sem1Sum/tempTableData.length);
  sem2Avg = (sem2Sum/tempTableData.length);
  sem1Percentage = Math.floor(((sem1Avg/(sem1Avg+sem2Avg))*100));
  sem2Percentage = Math.floor(((sem2Avg/(sem1Avg+sem2Avg))*100));
  percentageDiff = Math.abs(sem1Percentage - sem2Percentage);

  sem1Bar.style.height = sem1Percentage + "%";
  sem2Bar.style.height = sem2Percentage + "%";
  sem1Bar.innerHTML = sem1Percentage + "%";
  sem2Bar.innerHTML = sem2Percentage + "%";

  if (sem1Percentage > sem2Percentage) {
    analyticsSummary.innerHTML = "On average, semester 1 has a " + percentageDiff + " percent increase in grades over semester 2";
  }
  else {
    analyticsSummary.innerHTML = "On average, semester 2 has a " + percentageDiff + " percent increase in grades over semester 1";
  }


}


//---------------EVENT LISTENERS--------------------//
filterSortBttn.addEventListener("click", filterSort);
resetBttn.addEventListener("click", reset);





