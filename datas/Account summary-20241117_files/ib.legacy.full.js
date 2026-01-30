//Global Function for creating a namespace 
function registerNameSpace(ns)
{
    var nsParts = ns.split(".");
    var root = window;

    for (var i = 0; i < nsParts.length; i++)
    {
        if (typeof root[nsParts[i]] === "undefined") {
            root[nsParts[i]] = {};
        }

        root = root[nsParts[i]];
    }
}
//create default namespace 
nabiblegacy = {};//This popup code is configurable depending on how you have the attributes set
// Currency Utility Class
nabiblegacy.currencies = {
		
	balanceType : {
		CR: 'CR',
		DR: 'DR'
	},
	
	symbol : {
		AUD:'&#x24;',
		CAD:'&#x24;',
		EUR:'&#x20ac;',
		GBP:'&#xa3;',
		HKD:'&#x24;',
		JPY:'&#xa5;',
		NZD:'&#x24;',
		SGD:'&#x24;',
		THB:'&#xe3f;',
		USD:'&#x24;'
	},

	description : {
		AUD:'Australian Dollar',
		CAD:'Canadian Dollar',
		EUR:'Euro',
		GBP:'Pound Sterling',
		HKD:'Hong Kong Dollar',
		JPY:'Japanese Yen',
		NZD:'New Zealand Dollar',
		SGD:'Singapore Dollar',
		THB:'Thai Baht',
		USD:'United States Dollar'
	},

	decimalPlace : {
		AUD:2,
		CAD:2,
		EUR:2,
		GBP:2,
		HKD:2,
		JPY:0,
		NZD:2,
		SGD:2,
		THB:2,
		USD:2
	},
	
	getBalanceType : function (value) {
		return this.balanceType[value] ? this.balanceType[value] : '';
	},
	
	getSymbol : function (value) {
		return this.symbol[value] ? this.symbol[value] : '';
	},
	
	getDescription : function (value) {
		return this.description[value] ? this.description[value] : '';
	},
	
	toDecimalPlace : function (amount, currency) {
		var decimalPlace = this.decimalPlace[currency]!=undefined ? this.decimalPlace[currency] : 2;
		return parseFloat(Math.round(amount * 100) / 100).toFixed(decimalPlace).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
	},
	
	getSign : function (amount) {
		if (parseFloat(amount)<0) {
			return '-';
		} else {
			return '';
		}
	}
};
(function($){
	
	$.currencyConverter = function() {
		var curr = null;
		
		var exchangeRateUrl = "/nabib/exchange_rates_get_reference_rate.ctl";
		
		var calcRateChange = function(el, isAud) {
			var a, val = el.value || el.val();
			
			if(!isAud) {  
				a = val / curr.ttSellRate;
			} else {
				a = val * curr.ttSellRate;
			}
			
			if(isNaN(a)) { return 0; }
			
			return a.toFixed(2);
		};
		
		var onCurrencyChange = function(el) {
			var val = el.id;
			
			$("#currencyInput").val(val);
			
			$.ajax({
				url: exchangeRateUrl,
				dataType: "json",
				data: {currency: val},
				success: function(res) {
					curr = res;
					$("#rate").attr({value: calcRateChange($("#rate-aud"), true)});
					$("#rateInfo").text(curr.ttSellRate + " " + curr.currencyCode);
					$("#currencies").hide();
				},
				error: function(res) {
					$("#currencies").hide();
				}
			});
		};
		
		var onRateChange = function(el) {
			setTimeout(function() { 
				$("#rate-aud").val(calcRateChange(el));
			}, 500);
		};
		
		var onAudRateChange = function(el) {
			setTimeout(function() {
				$("#rate").val(calcRateChange(el, true));
			}, 500);
		};
		
		// init steps
		$("#currency, #ddArrow").click(function(e) { $("#currencies").toggle(); });
		$("#currencies a.currency").click(function(e) { 
			onCurrencyChange(e.target); 
			$("#currency").html(e.target.innerHTML);
			$("#currenciesDropdown").removeClass();
			$("#currenciesDropdown").addClass(e.target.id);
		});
		$("#rate").keypress(function(e) { onRateChange(e.target); });
		$("#rate-aud").keypress(function(e) { onAudRateChange(e.target); });
		$("#currency option:first-child").attr({selected: true});
		$("#USD").click();
	}
})(jQuery);// Date utility class for javascript

nabiblegacy.dateUtils = {
	
	yearPrefix: 20,
	
	monthShortened: [
					"Jan", "Feb", "Mar", "Apr",
					"May", "Jun", "Jul", "Aug",
					"Sep", "Oct", "Nov", "Dec"
	                ],
	
	// Input format: UTC
	// Output format: 12 Jan 13
	getDateMonthYear : function(date) {
		var utcDate = this.parseDate(date);
		return utcDate.getDate() + ' ' + this.monthShortened[utcDate.getMonth()] + ' ' + utcDate.getFullYear().toString().substring(2);
	},
	
	
	// Input format: UTC
	// Output format: 12 Jan 13
	getDateMonthFullYear : function(date) {
		var utcDate = this.parseDate(date);
		return utcDate.getDate() + ' ' + this.monthShortened[utcDate.getMonth()] + ' ' + utcDate.getFullYear().toString();
	},
		
	
	// Input format: 19/10/13
	// Output format: 20131019
	getNabApiDateFormat : function(date) {
		return this.yearPrefix + date.toString().substring(6) + date.toString().substring(3, 5) + date.toString().substring(0, 2);
	},
	
	// Returns UTC format date
	parseDate : function(date) {
		date = date.split(/\D/);
		var utcDate = new Date(Date.UTC(date[0], --date[1]||'', date[2]||'', date[3]||'', date[4]||'', date[5]||'', date[6]||''));
		return utcDate;
	}
}// $Revision: 1.5 $
// $Workfile: general.js $


NS4 = (document.layers);
IE4 = (document.all);
ver4 = (NS4 || IE4);
IE5 = (IE4 && navigator.appVersion.indexOf("5.")!=-1);
if( IE5 )
  IE4 = false;
isMac = (navigator.appVersion.indexOf("Mac") != -1);

//  This should NOT be commented out when going live
if(navigator.appName.indexOf("Microsoft") != -1)document.oncontextmenu=function(){return false}

var onKDHandler;
function initKey( handler ) {
  onKDHandler = handler;
  if(document.layers) {
    document.captureEvents(Event.KEYDOWN);
  }
  document.onkeydown =
  
  function(e) {
    whichASC = (navigator.appName == "Netscape") ? e.which : window.event.keyCode;
 	  if((whichASC==13) || (whichASC==3 && isMac)) {
			if (NS4) {
				var thisTarget = new String();
				thisTarget = String(e.target) 

				if (-1 == thisTarget.indexOf("textarea")) {
          return onKDHandler() 
        } else {
          return true
        }				
			} else {
        return onKDHandler()
      }
		}
	}
}

function init(){}

function disstatus()
{
  window.status = "";
  //function()
  //{return true;}
}

function getCookieVal(offset)
{
  var es = document.cookie.indexOf(";", offset);
  if(es==-1)es=document.cookie.length;
  return unescape(document.cookie.substring(offset,es));
}

function getCookie(name)
{
  var arg = name + "=";
  var alen = arg.length;
  var clen = document.cookie.length;
  var i = 0;
  while ( i < clen)
  {
    var j = i + alen;
    if (document.cookie.substring(i, j) == arg)
      return getCookieVal(j);
    i = document.cookie.indexOf(" ", i) + 1;
    if ( i == 0) break;
  }
  return null;
}

function createCookie(name,value,days) {
	if (days) {
		var date = new Date();
		date.setTime(date.getTime()+(days*24*60*60*1000));
		var expires = "; expires="+date.toGMTString();
	}
	else var expires = "";
	document.cookie = name+"="+value+expires+"; path=/";
}



/**
 * This is called by onUnload event to logout user if the user shutdowns the browser.
 * This is a 'hack' and it will not work in all possible circumstances. onUnload event
 * is called when (1) browser is paged, (2) browser is refreshed and (3) browser is closed.
 *
 * The logout process is only interested in catching the browser close event. It works by
 * opening a child window and detect if the parent window == null to determine if the
 * browser is closed. If the browser is closed, user loggout is sent.
 *
 * As a side effect, the child window is visible in NS, Safari and some mac browsers.
 * AFAIK, Safari 1.0 does not call onUnload event when the browser is closed, which defeats
 * this purpose.
 */
var canClose = true;
function logout()
{

  if(canClose) {
  	    // Send the child window away at the last pixel of the screen. In Safari, if it
  	    // is sent away more than the screen size, it is returned to 0,0. In NS, it is
  	    // bounded at the maximum. 
        
        //All browser will use these values as the default.
        var top = 4000;
        var left = 4000;
        
        //Safari will use the following values.
        if (isSafari)
        {
        	top = screen.height - 1;
        	left = screen.width - 1;
	    }

	    index = logouturl.indexOf("?sess");
	    if (index != -1) {
	    	logouturl = logouturl.substring(0,index);
	    }
	    window.open(logouturl,'logout','top=' + top + ',left=' + left + ',width=1,height=1');
  }
}

function sendMenuRequest(actionString){
  if( actionString.indexOf("javascript:") != -1)
  {
  	indexStart = actionString.indexOf(":");
  	jsFunc = actionString.substring(indexStart+1,actionString.length);
  	eval(jsFunc);
  	return;
  }
  
  if( !confirmCreateExit() ) return;
  if ( actionString == "logout.ctl" ){
    if (!confirm("Thank you for banking with NAB.\n Are you sure you want to exit Internet Banking?") ) return;
  }
  submitMenu(actionString);
  return;
}

function submitMenu(actionString)
{
  canClose = false;
  document.menuForm.action=actionString;
  document.menuForm.submit();
}

// Change the action of the first form of the page and submit it using the given error code as a parameter
function exitToErrorPage(errorCode)
{
  document.forms[0].action = "error_message.ctl?error=" + errorCode;
  document.forms[0].submit();
}

function stripCharsInBag (s, bag)
{
  re=new RegExp("["+bag+"]","g");
  return(s.replace(re,""));
}

function trimLeft(s){return (s.replace(/^\s+|\s+$/g,""));}

function trimCharacters(field, values) {
  var fvalue = field.value;
  return (stripCharsInBag(fvalue,values));
}

function validateNumber(field, valid) {
  var fvalue = trimLeft(field.value);
  var re = new RegExp("^[" + valid + "]+$");
  return (fvalue.match(re));
}

function validateWord(field, characters) {
  var fvalue = trimLeft(field.value);
  var re = new RegExp("^[" + characters + "]+$");
  return (fvalue.match(re));
}

function validateAlphaNumeric(field) {
  var fvalue = trimLeft(field.value);
  var re = new RegExp("^[0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]+$");
  return (fvalue.match(re));
}

function convertToDate(thatDate)
{
  var i = thatDate.indexOf("/");
  var j = thatDate.substring(i+1).indexOf("/") + i + 1;
  var theDate = thatDate.substring(0, i);
  var theMonth = thatDate.substring(i+1, j);
  var theYear = thatDate.substring(j+1);
  while (theMonth.substring(0, 1) == "0")
    theMonth = theMonth.substring(1);
  while (theDate.substring(0, 1) == "0")
    theDate = theDate.substring(1);

  if (theYear.length == 2)
      theYear = "20" + theYear;
  var resultDate = new Date(theYear, parseInt(theMonth)-1, parseInt(theDate)+1);
  return resultDate;
}

function formatAmount(amount)
{
  var amt = trimLeft(amount);
  if (amt.indexOf(".") == -1)
    amt = amt + ".00";

  if (amt.length < 7)
    return amt;

  var pos = amt.indexOf(".");
  var temp = amt.substring(pos);
  var num = (amt.length - 4 )/3;
  while (num > 0) {
    temp = amt.substring (pos -3, pos) + temp;
    num = num - 1;
    pos = pos - 3;
    if (num > 0) 
      temp = "," + temp;
    else if (pos > 0)
      temp = amt.substring(0, pos) + "," + temp;
  }
  return temp;
}

function validatePassword(field){
  var passwordStrength   = 0;
  var password = field.value;

  if ((password.length >0) && (password.length <=5)){ 
		passwordStrength=1;
  }else {
	  if (password.length >= 6) passwordStrength=1;
	
	  if (password.match(/[a-z]/)) passwordStrength++;
				
	  if (password.match(/[A-Z]/)) passwordStrength++;
	
	  if (password.match(/\d+/)) passwordStrength++;
	
	  if (password.match(/[^a-zA-Z0-9]/))	passwordStrength++;
  }
    
  return (passwordStrength >=3);
}

function validateMaxLengthPassword(field){
   var password = field.value;
   return (password.length >500);
}

function validateNum(field) {
  var reg1=/^[0-9]+$/;
  return reg1.test(field.value);
}

function validateNumber(field) {
  var reg1=/^[0-9]+$/;
  return reg1.test(field);
}

function validateAlphaNum(field) {
  var reg3=/^[0-9a-zA-Z\s\-\.\*\/]+$/;
  return reg3.test(field.value);
}

function validateDate(field) {
  var reg1=/^((([0]{1})+([1-9]{1}))|(([1-3]{1})+([\d]{1})))+\/+((([0]{1})+([1-9]{1}))|(([1]{1})+([0-2]{1})))+\/+(([0-9]{1})+([0-9]{1}))$/;
  if (reg1.test(field.value) == true)
    return isDateValid(field.value);
  return false;
}

function isDateValid(dateStr)
{
  var len = dateStr.length;
  if (len == 0)
    return false;
  var datePat = /^(\d{1,2})(\/)(\d{1,2})\2(\d{2}|\d{4})$/;
  var matchArray = dateStr.match(datePat);
  if (matchArray == null) 
    return false;
  month = matchArray[3];
  day = matchArray[1];
  year = matchArray[4];

  if( month.length != 2 || day.length != 2 || (year.length != 2 && year.length != 4) )
    return false;
  if (month < 1 || month > 12)
    return false;

  if (day < 1 || day > 31) 
    return false;
  if ((month==4 || month==6 || month==9 || month==11) && day==31)
    return false;
  if (month == 2)
  { 
    var isleap = (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0));
    if (day>29 || (day==29 && !isleap)) 
      return false;
  }
  return true;
}

function validateDecimal(field){
	if(!isNaN(field))
	{
 		var reg1=/^[0-9\.]+$/;
	  	return reg1.test(field);
	}
	else
		return false;
}

function validateZero(field){
  var reg1=/^0*[1-9][0-9]*$/;
  return reg1.test(field.value);
}

function isNonZeroInteger(field)
{
  var reg1=/^[1-9]{1,}[0-9]*$/
  return reg1.test(field.value);
}

function validateTele(field) 
{
  var reg1=/^[0-9a-zA-Z\s\-\(\)\+]+$/;
  return reg1.test(field.value);
}

function validateBSB(field)
{
  var reg1=/^[0]{1,6}$/
  return !reg1.test(field.value);
}

function reformatDate(newDate)
{
  var reg2 = /^(\d{1,2})(\/|-)(\d{1,2})\2(\d{2}|\d{4})$/;
  var matchArray = newDate.match(reg2);
  var month = matchArray[3];
  var day = matchArray[1];
  var year = matchArray[4];
  var month2 = month - 1;
  if ((year >= 00) && (year < 70)){
  year = '2' + '0' + year;
  DateOne = new Date(Date.UTC( year, month2, day));
  valueDate = DateOne.valueOf();
  return valueDate;
  }
  else if ((year >= 70) && (year <= 99)){
  year = '1' + '9' + year;
  DateOne = new Date(Date.UTC( year, month2, day));
  valueDate = DateOne.valueOf();
  return valueDate;
  }
}

function isEmpty(s){return ((s == null) || (s.length == 0))}

function isDigit(c){return ((c >= "0") && (c <= "9"))}

/**
 * This function will return true if the array contains the specified value, otherwise false.
 * arrayVar - Array of values
 * valueVar - Value to search on
 */
function containsValue(arrayVar, valueVar)
{
    var found = false;
    for (j=0; j<arrayVar.length; j++)
    {
        if (arrayVar[j] == valueVar)
        {
            found = true;
            break;
        }
    }
    
    return found;
}
/*
	Do an asynchronous call to a URL.
	
	This function make an asynchronous call to the supplied URL
	(getURL).

	When the call returns, the supplied method is called to process the data
	(readyStateChangeFunction).  The method should accept an httpRequest as
	its single argument.
	
	If you do not need to process the returned data, supply a null for the
	callback function.
*/

function asynchGet(getURL, readyStateChangeFunction) {

	var httpRequest;

	if (window.XMLHttpRequest) { // Mozilla, Safari, ...
		httpRequest = new XMLHttpRequest();
	} 
	else if (window.ActiveXObject) { // IE
		try {
			httpRequest = new ActiveXObject("Msxml2.XMLHTTP");
		}
		catch (e) {
			try {
				httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
			}
			catch (e) {}
		}
	}

	if (!httpRequest) {
		return false;
	}
	
	// Assign the callback function to process the returned data.
	// See asynchGetDataProcess() below for an example.
	
	if (readyStateChangeFunction != null) {
		httpRequest.onreadystatechange = function() { readyStateChangeFunction(httpRequest); };
	}
		
	// Go ahead and make the call (async == true).
	
	httpRequest.open("GET", getURL, true);
	httpRequest.send("");
}

/*
	An example of a callback method to supply to the asynchGet function.  Note
	that these callbacks have to accept an httpRequest object instance as their
	first and only argument.
*/

function asynchGetDataProcess(httpRequest) {

	if (httpRequest.readyState == 4) {
	
		if (httpRequest.status == 200) {
			alert(httpRequest.responseText);
		}
		else {
			alert("There was a problem with the request.");
		}
	}
}

function check(p,k,a) {
  return encode(p,k,a);
}

// returns true if parameter supplied to function is numeric
function IsNumeric(sText)
{
   var ValidChars = "0123456789";
   var IsNumber=true;
   var Char;

 
   for (i = 0; i < sText.length && IsNumber == true; i++) { 
      Char = sText.charAt(i); 
      if (ValidChars.indexOf(Char) == -1) {
         IsNumber = false;
      }
    }
   return IsNumber;
}

/* 
 * Performs page URL nagivation and ensuring there is a HTTP referer.
 *
 * Regular location.href is problematic because IE don't carry referer
 * during location.href. 
 *
 * This implementation dynamically creates a form '#navigateTo'
 * and configures the correct form action and parameters based
 * on a URL with valid query string parameter. The form is automatically
 * submitted to emulate a page navigation behaviour. Using this
 * approach all tested browsers appear to supply HTTP REFERER.
 *
 * This also used by the generated javascript in ConfirmTag.java.
 * This method REQUIRES JQUERY to function.
 */
function navigateTo(url) {
	// Parse the url
	// querystring[0] => url to reach
	// querystring[1] => querystring of parameters
	var querystring = url.split("?");
	
	// Create the navigational form ONLY if it does not exist.
	if ($("#navigateTo").html() == null) {
		$("body")
		.append("<form id='navigateTo' method='GET'></form>");
	}
		
	// Clear it, because an old one may be there
	$("#navigateTo").empty();
	
	// Specifies the desired URL to reach
	$("#navigateTo").attr("action",querystring[0]);		
	
	// Populate hidden input parameters from queryString format
	if (querystring.length > 1) {	
		var params = querystring[1].split("&");
		for (var i=0;i<params.length;i++) {
			var pair = params[i].split("=");
			$("#navigateTo").append("<input type='hidden' name='" + pair[0] + "' value='" + pair[1] + "'>");
		}	
	}
	
	// Submit it
	$("#navigateTo").get(0).submit();	
}

/* 
 * Tells the browser to alert after a small delay. This is needed in IE when the page contains
 * some jquery rules and css stylng rules. The regular popup stops the styling from completing
 * when the popup block the screen. 
 *
 * Use for showing popup alert when the page is being loaded.
 */
function onLoadAlert(message) {
	window.setTimeout(function() {
		alert(message);
	}, 300);    
}

/* Returns IB window width (in a browser compatible manner)
 */
function browserWidth() {
	return window.innerWidth != null? window.innerWidth : document.documentElement && document.documentElement.clientWidth ?       
		   document.documentElement.clientWidth : document.body != null ? document.body.clientWidth : null;
} 

/* Returns IB window height (in a browser compatible manner)
 */
function browserHeight() {
	return window.innerHeight != null? window.innerHeight : document.documentElement && document.documentElement.clientHeight ?  
		   document.documentElement.clientHeight : document.body != null? document.body.clientHeight : null;
}


/**
 * Sets "ibWindowSize" cookie: value is left/X coordinate + "x" + top/Y coordinate
 * Used by registration process to size windows to allow for first time user wizard.
 */
function setIBWindowCoordCookie() {
	var ibWinSize = "";
	var exp = new Date();
	var currDate = exp.getTime();
	var newExpDate = currDate + (182 * 24 * 60 * 60 * 1000);
	exp.setTime(newExpDate);

	var winX=0;
	var winY=0;

	if($.browser.msie){
		winX=window.screenLeft;
		winY=window.screenTop;
	} else {
		winX=window.screenX;
		winY=window.screenY;
	}
	
	ibWinSize = winX+"x"+winY;
	document.cookie = "ibWindowSize=" + ibWinSize + "; expires=" + exp.toGMTString() + "; path=/";
}

/**
 * Gets "ibWindowSize" cookie: value is left/X coordinate + "x" + top/Y coordinate
 * Used by registration process to size windows to allow for first time user wizard.
 */
function getIBWindowCoordCookie() {
	var nameEq = "ibWindowSize=";
	var ca = document.cookie.split(';');
	for(var i=0;i < ca.length;i++){
		var c = ca[i];
		while (c.charAt(0)==' ') c = c.substring(1,c.length);
		if (c.indexOf(nameEq) == 0) return c.substring(nameEq.length,c.length);
	}
	return null;
}

/**
 * As user types into textbox, restricts input to digits and decimal point
 * usage: onkeypress="return restrictCurrencyInput(event);"
 */
function restrictCurrencyInput(evt) {
	var charCode = (evt.which) ? evt.which : event.keyCode;
	if (charCode != 46 && charCode > 31 && (charCode < 48 || charCode > 57)) {
		return false;
	}
	return true;
}

/**
 * As user types into textbox, restricts input to digits only
 * usage: onkeypress="return restrictDigitInput(event);"
 */
function restrictDigitInput(evt)
{
	var charCode = (evt.which) ? evt.which : event.keyCode
	if (charCode > 31 && (charCode < 48 || charCode > 57))
	   return false;
	
	return true;
}

function imgError(source) {    
	source.onerror ="";
	source.src ="images/blank.gif";
	source.style.border = "none";
	return true;
}

function test() {
	return false;
}

//Large clipboard pastes and other outlier scenarios to be handled by server side validation or onchange/onkeyup handlers
function limitLength(evt, obj, limit){
	if(obj.value.length > limit-1){
		var c = (evt.which) ? evt.which : event.keyCode;
		return (c==8||(c>32&&c<41)||c==46||(evt.ctrlKey&&(c==67||c==88)));
	}		
}

$(function() {
	/**
	 * This click_once is to prevent duplicate form submissions.
	 * You can apply this to all the button classes.
	 */
	//$('.click_once').click(function() {
	//	$(this).attr("disabled", "true");
	//});   
	
	$(".click_once").parents('form').submit(function(){
		$(".click_once").attr('disabled', 'true');
	});

});

(function($) {
  $.fn.nabExpandableText = function(short, long) {
    $(long).hide();
    $(this).click(function () {
      $(this).hide();
      $(short).hide();
      $(long).show();
    });
  }
})(jQuery);

function removeSpaces(string) {
	return string.replace(/\s/g, "");
}

function removeLeadingTrailingSpaces(string) {
	return string.replace(/(^\s+|\s+$)/g, "");
}

function sortBy(prop) {
	return function(a, b) {
		if (a[prop] > b[prop]) {
			return 1;
		} else if (a[prop] < b[prop]) {
			return -1;
		}
		return 0;
	}
}

function showAlertPopup(messageString) {
	if (messageString.length > 0) {	
		onLoadAlert(messageString);
	}
}
// in the following format:
//     ('genURL', 'extwinName', 'windowwidth', 'windowheight', 'scrollbars', 'toolbar', 'menubar', 'resizable', 'status', 'directories')
//     Where 	genURL 		= the html page that appears in the popup
//                extwinName 	= a name you give to the window
//                windowwidth 	= window width
//                windowheight 	= window height
//                scrollbars 	= yes or no
//                toolbar 		= yes or no
//                menubar 		= yes or no
//                resizeable 	= yes or no
//                status 		= yes or no
//                directories 	= yes or no
//                left          = pixels window appears from left of screen
//                top           = pixels window appears from top of screen
//                location    = display location bar. Yes to display, no or blank for don't display.

function openPopUpWindow(genURL, extwinName, windowwidth, windowheight, scrollbars, toolbar, menubar, resizable, status, directories, left, top, location)	{

	var generatedURL = genURL;
	var winName      = extwinName;
	var targetFound  = false;
	var idx          = opnwinIdx;
	var eleName      = null;
	var eleReff      = null;
   var winWidth 	 = windowwidth;
	var winHeight 	 = windowheight;
   var winScroll    = scrollbars;
   var winToolbar   = toolbar;
   var winMenubar   = menubar;
   var winResizable = resizable;
   var winStatus    = status;
   var winDirectories = directories;
   var winScreenX   = left;
   var winScreenY   = top;
   var location1 = (location == "yes") ? "yes" : "no";

	var options = "width=" + winWidth + ",height=" + winHeight +  ",scrollbars=" + winScroll + ",";
		 options += "toolbar=" + winToolbar + ",menubar=" + winMenubar + ",";
       options += "resizable=" + winResizable + ",status=" + winStatus + ",";
       options += "directories=" + winDirectories + ",";
       options += "screenX=" + winScreenX + ",screenY=" + winScreenY + ",";
       options += "left=" + winScreenX + ",top=" + winScreenY + ",";
		 options += "location=" + location1 + ", channelmode=no,";

		// The following lines are for tracking multiple windows being opened.
		var opnwinNameArray = new Array();
        var opnwinIDArray = new Array();
		var eleReference = null;
		var opnwinIdx = 0;

		function selectedValue(control) {
			return control.options[control.selectedIndex].value;
		}


		// Search the array to see if the target window already exits.
		for(var i=0; i < idx; i++)
		{
			eleName = opnwinNameArray[i]

			// if there is a match, exit the for loop, else set the temp varibles to blanks.
			if (eleName == winName) {
				eleReff = opnwinIDArray[i]
				targetFound = true;
				break;
			}
			else
			{
				eleName = "";
			}
		}

		// Check to see if the target is empty or closed. If so then a new window will be opened. If not
		// then the window already is opened and the focus will be shifted to it.

	    if (targetFound) {
			if ((eleReff == null) || (eleReff.closed))
			{
				opnwinIDArray[i] = window.open(generatedURL, winName, options);
				self.opnwinIDArray[i].focus();
			}
			else
			{
				self.opnwinIDArray[i].focus();
			}
		}
		else
		{
			// If the target window is new, add it to the open windows arrays.
			opnwinIDArray[opnwinIdx] = window.open(generatedURL, winName,  options)
			opnwinNameArray[opnwinIdx] = winName;
			opnwinIdx = ++idx;
		}
	}