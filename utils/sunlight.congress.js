// Tait Wayland
// Code for Birmingham

// Documentation for Sunlight congress API at https://sunlightlabs.github.io/congress
// For this to work you'll need to replace userKey with your API key.

var userKey = 'put-api-key-here',
APIcall = 'https://congress.api.sunlightfoundation.com/',
keyConfirm = '?apikey=[your_api_key]',
keyConfirm = keyConfirm.replace("[your_api_key]", userKey);

function httpGet(theUrl)
{
    var xmlHttp = null;

    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send( null );
    return xmlHttp.responseText;
};

searchLegislators = function(constraints) {
        var fieldsParam;
        for(var i = 0; i < arguments.length; i++) {
          fieldsParam += '&' + arguments[i];
        }
        httpGet(APIcall + 'legislators'+ keyConfirm + '&' + fieldsParam);
}

searchLegislators('lastname=shelby', 'fields=fec_ids');
