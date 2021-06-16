#!/bin/bash

# Set some default values:
CHROME=`find . -name 'chrome*.*'`
FIREFOX=`find . -name 'gecko*.*'`
EDGE=`find . -name '*edge*.*'`
REMOTEIP="http://127.0.0.1:4444"
JARFILE=`find . -name '*.jar'`

usage()
{
  echo "Usage: alphabet"
  echo "[ -c | --chromedriver ] - Chrome driver path"
  echo "[ -e | --edgedriver ]   - Edge driver path"
  echo "[ -g | --geckodriver ]  - Gecko driver path"
  echo "[ -r | --remoteip ]     - Remote Selenium grid register url with port (default $REMOTEIP)"
  echo "[ -f ]                  - Selenium standalone server ".jar" file path"
  exit 2
}

PARSED_ARGUMENTS=$(getopt -a -n alphabet -o c:g:e:r:f:h: --long file,chromedriver,geckodriver,edgedriver,remoteip -- "$@")
VALID_ARGUMENTS=$?
if [ "$VALID_ARGUMENTS" != "0" ]; then
  usage
fi

echo "PARSED_ARGUMENTS is $PARSED_ARGUMENTS"
eval set -- "$PARSED_ARGUMENTS"
while :
do
  case "$1" in
	-f)   JARFILE="$2"   ; shift 2 ;;
    -c | --chromedriver)   CHROME="$2"      ; shift 2 ;;
    -g | --geckodriver)    FIREFOX="$2"       ; shift 2 ;;
    -e | --edgedriver) EDGE="$2" ; shift 2 ;;
    -r | --remoteip)   REMOTEIP="$2"   ; shift 2 ;;
    --) shift; break ;;
    -h | --help) echo "Unexpected option: $1 - this should not happen."
       usage ;;
  esac
done
SELENIUM_SERVER_COMMAND="java "
BROWSER_SETTINGS=""

if [ -n CHROME ]; then
	SELENIUM_SERVER_COMMAND=$SELENIUM_SERVER_COMMAND"-Dwebdriver.chrome.driver="\"${CHROME}\"
	BROWSER_CHROME_MAX_INSTANCE="browserName=chrome,maxInstances=5"
	BROWSER_SETTINGS=$BROWSER_SETTINGS" -browser "\"${BROWSER_CHROME_MAX_INSTANCE}\"
fi
if [ -n FIREFOX ]; then
	SELENIUM_SERVER_COMMAND=$SELENIUM_SERVER_COMMAND" -Dwebdriver.gecko.driver="\"${FIREFOX}\"
	BROWSER_FIREFOX_MAX_INSTANCE="browserName=firefox,maxInstances=5"
	BROWSER_SETTINGS=$BROWSER_SETTINGS" -browser "\"${BROWSER_FIREFOX_MAX_INSTANCE}\"
fi
if [ -n EDGE ]; then
	SELENIUM_SERVER_COMMAND=$SELENIUM_SERVER_COMMAND" -Dwebdriver.edge.driver="\"${EDGE}\"
	BROWSER_EDGE_MAX_INSTANCE="browserName=MicrosoftEdge,maxInstances=5"
	BROWSER_SETTINGS=$BROWSER_SETTINGS" -browser "\"${BROWSER_EDGE_MAX_INSTANCE}\"
fi

if [ -n JARFILE ]; then
	SELENIUM_SERVER_COMMAND=$SELENIUM_SERVER_COMMAND" -jar "$JARFILE" "
	else
		echo "Please check current directory, because no have executable .jar file!"
fi
SELENIUM_SERVER_COMMAND=$SELENIUM_SERVER_COMMAND" "$BROWSER_SETTINGS
REGISTER_STRING=" -role node -hub "
SELENIUM_SERVER_COMMAND=$SELENIUM_SERVER_COMMAND$REGISTER_STRING$REMOTEIP"/grid/register"


echo ""
echo "==========================================="
echo "SETTINGS"
echo "==========================================="
echo "CHROME DRIVER  : $CHROME"
echo "FIREFOX DRIVER : $FIREFOX"
echo "EDGE DRIVER    : $EDGE"
echo "REMOTE IP      : $REMOTEIP"
echo "SELENIUM GRID  : $JARFILE"
echo ""

echo "==========================================="
echo "SELENIUM GRID - REGISTER NODE COMMAND"
echo "==========================================="
echo $SELENIUM_SERVER_COMMAND
echo ""

eval $SELENIUM_SERVER_COMMAND
