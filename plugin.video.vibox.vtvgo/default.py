#!/usr/bin/python
# coding=utf-8
import urllib , requests , re , json , HTMLParser , os , uuid , datetime , time
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
requests . packages . urllib3 . disable_warnings ( )
oo000 = Plugin ( )
ii = HTMLParser . HTMLParser ( )
oOOo = "plugin://plugin.video.vibox.vtvgo"
if 59 - 59: Oo0Ooo . OO0OO0O0O0 * iiiIIii1IIi . iII111iiiii11 % I1IiiI
IIi1IiiiI1Ii = "http://echipstore.com:8000/vntime"
if 39 - 39: O0 - ooOO00oOo % oOo0O0Ooo * Ooo00oOo00o . oOoO0oo0OOOo + iiiiIi11i
def Ii1I ( s ) :
 s = '' . join ( s . splitlines ( ) ) . replace ( '\'' , '"' )
 s = s . replace ( '\n' , '' )
 s = s . replace ( '\t' , '' )
 s = re . sub ( '  +' , ' ' , s )
 s = s . replace ( '> <' , '><' )
 return ii . unescape ( s )
 if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
@ oo000 . route ( '/list_date/<args_json>' )
def O0oOO0o0 ( args_json = { } ) :
 i1ii1iIII = [ ]
 Oo0oO0oo0oO00 = json . loads ( args_json )
 i111I = requests . get ( IIi1IiiiI1Ii ) . text
 Oo0oO0oo0oO00 [ "date" ] = i111I [ : 10 ] . replace ( "-" , "" )
 II1Ii1iI1i (
 "[List date] from %s" % (
 Oo0oO0oo0oO00 [ "date" ]
 ) ,
 '/list_date/%s/%s' % (
 Oo0oO0oo0oO00 [ "url" ] ,
 json . dumps ( Oo0oO0oo0oO00 [ "payloads" ] ) if "payloads" in Oo0oO0oo0oO00 else "{}"
 )
 )
 if 12 - 12: o0oOoO00o
 i1 = datetime . datetime ( year = 2016 , month = 1 , day = 1 )
 if 64 - 64: oo % O0Oooo00
 if 87 - 87: i1IIi11111i / ooOO00oOo % o0oOoO00o * o0oOoO00o * o00O0oo / iiiIIii1IIi
 if 88 - 88: o0oOoO00o / ooOO00oOo + I1IiiI % iII111iiiii11 . oo / i1IIi11111i
 try :
  I1I1i1 = datetime . datetime . strptime ( i111I , "%Y-%m-%d %H:%M" )
 except TypeError :
  I1I1i1 = datetime . datetime ( * ( time . strptime ( i111I , "%Y-%m-%d %H:%M" ) [ 0 : 6 ] ) )
  if 18 - 18: iiiIIii1IIi / ooOoO0o + IiII / oOo0O0Ooo - O0 - ooOoO0o
 for I111IiIi in xrange ( 1 , ( I1I1i1 - i1 ) . days ) :
  IiiIIiiI11 = { }
  OOooO = ( I1I1i1 - datetime . timedelta ( days = I111IiIi ) )
  IiiIIiiI11 [ "label" ] = "%s %s" % ( OOooO . strftime ( "%Y-%m-%d" ) , Oo0oO0oo0oO00 [ "title" ] )
  OOoO00o = {
 "title" : Oo0oO0oo0oO00 [ "title" ] ,
 "url" : Oo0oO0oo0oO00 [ "url" ] ,
 "date" : OOooO . strftime ( "%Y%m%d" ) ,
 "channel_id" : Oo0oO0oo0oO00 [ "channel_id" ]
 }
  IiiIIiiI11 [ "path" ] = '%s/list_media/%s' % (
 oOOo ,
 urllib . quote_plus ( json . dumps ( OOoO00o ) )
 )
  IiiIIiiI11 [ "thumbnail" ] = "https://docs.google.com/drawings/d/16wuwv1LBUL030G13aypfrRxpQ8rs6b011WnQc_uF0z4/pub?w=256&h=256"
  i1ii1iIII . append ( IiiIIiiI11 )
 if oo000 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return oo000 . finish ( i1ii1iIII , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return oo000 . finish ( i1ii1iIII , view_mode = 52 )
  else :
   return oo000 . finish ( i1ii1iIII )
 else :
  return oo000 . finish ( i1ii1iIII )
  if 9 - 9: ooOO00oOo - o00O0oo % I1IiiI % iII111iiiii11
  if 3 - 3: o0oOoO00o + OO0OO0O0O0
@ oo000 . route ( '/list_media/<args_json>' )
def I1Ii ( args_json = { } ) :
 i1ii1iIII = [ ]
 Oo0oO0oo0oO00 = json . loads ( args_json )
 o0oOo0Ooo0O = "%s-%s-%s" % (
 Oo0oO0oo0oO00 [ "date" ] [ : 4 ] ,
 Oo0oO0oo0oO00 [ "date" ] [ 4 : 6 ] ,
 Oo0oO0oo0oO00 [ "date" ] [ 6 : ]
 )
 if Oo0oO0oo0oO00 [ "date" ] == "" :
  o0oOo0Ooo0O = requests . get ( IIi1IiiiI1Ii ) . text
  Oo0oO0oo0oO00 [ "date" ] = o0oOo0Ooo0O [ : 10 ] . replace ( "-" , "" )
 OO00O0O0O00Oo = requests . get ( Oo0oO0oo0oO00 [ "url" ] % ( Oo0oO0oo0oO00 [ "date" ] , Oo0oO0oo0oO00 [ "channel_id" ] ) ) . text
 II1Ii1iI1i (
 "[Browse Media of] %s" % (
 Oo0oO0oo0oO00 [ "title" ] if "title" in Oo0oO0oo0oO00 else "Unknow Title"
 ) ,
 '/list_media/%s/%s' % (
 Oo0oO0oo0oO00 [ "url" ] ,
 json . dumps ( Oo0oO0oo0oO00 [ "payloads" ] ) if "payloads" in Oo0oO0oo0oO00 else "{}"
 )
 )
 IIIiiiiiIii = OO00O0O0O00Oo [ 1 : - 1 ] . decode ( "unicode-escape" ) . replace ( "\\" , "" )
 IIIiiiiiIii = Ii1I ( IIIiiiiiIii )
 if 70 - 70: Ooo00oOo00o . Ooo00oOo00o - Ooo00oOo00o / iII111i * I1Ii111
 for OoO000 , IIiiIiI1 , iiIiIIi , ooOoo0O in re . compile ( 'data-epgid="(.+?)" data-title="(.+?)" data-type="(.+?)" data-id=".+?"><label>(.+?)</label>' ) . findall ( IIIiiiiiIii ) :
  IiiIIiiI11 = { }
  OooO0 = "http://vtvgo.vn/get-program-channel-detail?epg_id=%s&id=%s&type=%s"
  IiiIIiiI11 [ "label" ] = IIiiIiI1
  if iiIiIIi == "1" :
   OoO000 = Oo0oO0oo0oO00 [ "channel_id" ]
   IiiIIiiI11 [ "label" ] = "[B]%s %s[/B]: [COLOR yellow](Đang chiếu...) %s[/COLOR]" % (
 o0oOo0Ooo0O . encode ( "utf8" ) ,
 Oo0oO0oo0oO00 [ "title" ] . encode ( "utf8" ) ,
 IIiiIiI1 . encode ( "utf8" )
 )
   IiiIIiiI11 [ "thumbnail" ] = "https://docs.google.com/drawings/d/1D062LFwy5mutvBd1LpByb_S-PfcrPyetYPaH-hbfiwY/pub?w=256&h=256"
  else :
   IiiIIiiI11 [ "label" ] = "[B]%s %s %s[/B]: [COLOR green]%s[/COLOR]" % (
 o0oOo0Ooo0O [ : 10 ] . encode ( "utf8" ) ,
 ooOoo0O . encode ( "utf8" ) ,
 Oo0oO0oo0oO00 [ "title" ] . encode ( "utf8" ) ,
 IIiiIiI1 . encode ( "utf8" )
 )
   IiiIIiiI11 [ "thumbnail" ] = "https://docs.google.com/drawings/d/16wuwv1LBUL030G13aypfrRxpQ8rs6b011WnQc_uF0z4/pub?w=256&h=256"
  OooO0 = OooO0 % ( OoO000 , Oo0oO0oo0oO00 [ "channel_id" ] , iiIiIIi )
  OOoO00o = {
 "title" : re . sub ( "\[.+?\]" , "" , IiiIIiiI11 [ "label" ] ) ,
 "url" : OooO0
 }
  IiiIIiiI11 [ "path" ] = '%s/play/%s' % (
 oOOo ,
 urllib . quote_plus ( json . dumps ( OOoO00o ) )
 )
  IiiIIiiI11 [ "is_playable" ] = True
  i1ii1iIII . append ( IiiIIiiI11 )
 i1ii1iIII . reverse ( )
 if len ( i1ii1iIII ) == 0 :
  OooO0 = "http://vtvgo.vn/get-program-channel-detail?epg_id=%s&id=%s&type=1" % ( Oo0oO0oo0oO00 [ "channel_id" ] , Oo0oO0oo0oO00 [ "channel_id" ] )
  IiiIIiiI11 = { }
  IiiIIiiI11 [ "label" ] = "[B]%s %s[/B]: [COLOR yellow](Đang chiếu...) %s[/COLOR]" % (
 o0oOo0Ooo0O . encode ( "utf8" ) ,
 Oo0oO0oo0oO00 [ "title" ] . encode ( "utf8" ) ,
 ""
 )
  OOoO00o = {
 "title" : re . sub ( "\[.+?\]" , "" , IiiIIiiI11 [ "label" ] ) ,
 "url" : OooO0
 }
  IiiIIiiI11 [ "path" ] = '%s/play/%s' % (
 oOOo ,
 urllib . quote_plus ( json . dumps ( OOoO00o ) )
 )
  IiiIIiiI11 [ "thumbnail" ] = "https://docs.google.com/drawings/d/1D062LFwy5mutvBd1LpByb_S-PfcrPyetYPaH-hbfiwY/pub?w=256&h=256"
  IiiIIiiI11 [ "is_playable" ] = True
  i1ii1iIII . append ( IiiIIiiI11 )
 II11iiii1Ii = { }
 II11iiii1Ii [ "label" ] = "Xem thêm..."
 II11iiii1Ii [ "path" ] = '%s/list_date/%s' % (
 oOOo ,
 urllib . quote_plus ( json . dumps ( Oo0oO0oo0oO00 ) )
 )
 II11iiii1Ii [ "thumbnail" ] = "https://docs.google.com/drawings/d/16wuwv1LBUL030G13aypfrRxpQ8rs6b011WnQc_uF0z4/pub?w=256&h=256"
 i1ii1iIII . append ( II11iiii1Ii )
 if oo000 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return oo000 . finish ( i1ii1iIII , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return oo000 . finish ( i1ii1iIII , view_mode = 52 )
  else :
   return oo000 . finish ( i1ii1iIII )
 else :
  return oo000 . finish ( i1ii1iIII )
  if 70 - 70: IiII / iiiIIii1IIi % i1IIi11111i % Oo0Ooo . ooOO00oOo
@ oo000 . route ( '/play/<args_json>' )
def O0o0Oo ( args_json = { } ) :
 Oo0oO0oo0oO00 = json . loads ( args_json )
 II1Ii1iI1i (
 "[Play] %s" % (
 Oo0oO0oo0oO00 [ "title" ] . encode ( "utf8" ) if "title" in Oo0oO0oo0oO00 else "Unknow Title"
 ) ,
 '/play/%s/%s' % (
 Oo0oO0oo0oO00 [ "url" ] ,
 json . dumps ( Oo0oO0oo0oO00 [ "payloads" ] ) if "payloads" in Oo0oO0oo0oO00 else "{}"
 )
 )
 Oo00OOOOO = xbmcgui . DialogProgress ( )
 Oo00OOOOO . create ( 'VTVGo' , 'Đang tải, Xin quý khách vui lòn đợi trong giây lát...' )
 oo000 . set_resolved_url ( O0O ( Oo0oO0oo0oO00 [ "url" ] ) , subtitles = "https://docs.google.com/spreadsheets/d/16l-nMNyOvrtu4FKLm-ctGDNClCjI09XKp3lcOKPOXMk/export?format=tsv&gid=0" )
 Oo00OOOOO . close ( )
 del Oo00OOOOO
 if 83 - 83: ooOoO0o + O0 * iiiiIi11i % Ooo00oOo00o + ooOoO0o
def O0O ( url ) :
 url = url . replace ( "get-program-channel?" , "get-program-channel-detail?" )
 Ii1iIIIi1ii = {
 "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36" ,
 "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8" ,
 "Accept-Encoding" : "gzip, deflate" ,
 "Referer" : "http://vtvgo.vn/" ,
 }
 if 80 - 80: ooOoO0o * Oo0Ooo / O0Oooo00
 I11II1i = requests . get ( "aHR0cDovL3Z0dmdvLnZuL3hlbS10cnVjLXR1eWVuLmh0bWw=" . decode ( "base64" ) , headers = Ii1iIIIi1ii )
 IIIII = re . compile ( "'(\w{32})'\)\;" ) . findall ( I11II1i . text . encode ( "utf8" ) ) [ 0 ]
 try :
  ooooooO0oo = "|Referer=http%3A%2F%2Fvtvgo.vn%2F"
  OoO000 = re . compile ( 'epg_id=(\d+)' ) . findall ( url ) [ 0 ]
  IIiiiiiiIi1I1 = re . compile ( 'type=(\d+)' ) . findall ( url ) [ 0 ]
  Ii1iIIIi1ii = {
 "X-Requested-With" : "XMLHttpRequest" ,
 "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36" ,
 "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8" ,
 "Accept-Encoding" : "gzip, deflate" ,
 "Referer" : "http://vtvgo.vn/" ,
 "Cookie" : "csrf_security=1"
 }
  I1IIIii = {
 "epg_id" : OoO000 ,
 "type" : IIiiiiiiIi1I1 ,
 "secret_token" : IIIII ,
 "csrf_security" : "1"
 }
  oOoOooOo0o0 = requests . post ( url , headers = Ii1iIIIi1ii , data = I1IIIii ) . json ( )
  return oOoOooOo0o0 [ "data" ] + ooooooO0oo
 except :
  return None
  if 61 - 61: iiiiIi11i / Ooo00oOo00o + i1IIi11111i * IiII / IiII
def II1Ii1iI1i ( title = "Home" , page = "/" ) :
 OoOo = "http://www.google-analytics.com/collect"
 iI = open ( o00O ) . read ( )
 I1IIIii = {
 'v' : '1' ,
 'tid' : 'UA-52209804-5' ,
 'cid' : iI ,
 't' : 'pageview' ,
 'dp' : "VTVGo" + page ,
 'dt' : "[VTVGo] - %s" % title
 }
 requests . post ( OoOo , data = urllib . urlencode ( I1IIIii ) )
 if 69 - 69: IiII % O0Oooo00 - iiiiIi11i + O0Oooo00 - OO0OO0O0O0 % iII111iiiii11
Iii111II = xbmc . translatePath ( 'special://userdata' )
if os . path . exists ( Iii111II ) == False :
 os . mkdir ( Iii111II )
o00O = os . path . join ( Iii111II , 'cid' )
if 9 - 9: Ooo00oOo00o
if os . path . exists ( o00O ) == False :
 with open ( o00O , "w" ) as i11 :
  i11 . write ( str ( uuid . uuid1 ( ) ) )
  if 58 - 58: I1Ii111 * Oo0Ooo / oOoO0oo0OOOo % O0Oooo00 - iII111i / IiII
if __name__ == '__main__' :
 oo000 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
