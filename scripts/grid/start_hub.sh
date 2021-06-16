#!/bin/bash
# Set some default values:

JARFILE=`find . -name '*.jar'`
PORT=""

usage()
{
  echo "==========================================="
  echo "COMMAND PARAMETER HELP"
  echo "==========================================="
  echo "[ -p ]  - Hub Server start up port"
  echo "[ -f ]  - Selenium standalone server ".jar" file path"
  exit 2
}

PARSED_ARGUMENTS=$(getopt -a -n alphabet -o :f:i:p:h: --long help -- "$@")
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
	-p)   PORT="$2"   ; shift 2 ;;
    --) shift; break ;;
    -h | --help) echo "Unexpected option: $1 - this should not happen."
       usage ;;
  esac
done

SELENIUM_SERVER_COMMAND="java -jar "

if [ -n JARFILE ]; then
	SELENIUM_SERVER_COMMAND=$SELENIUM_SERVER_COMMAND$JARFILE" -role hub "
else
	echo "Please check current directory, because no have executable .jar file!"
fi

if [ ! -n "$PORT" ]; then
	 PORT="4444"
else
	 SELENIUM_SERVER_COMMAND=$SELENIUM_SERVER_COMMAND" -port $PORT"
fi


REGISTER_STRING=" -role hub"
SELENIUM_SERVER_COMMAND=$SELENIUM_SERVER_COMMAND


echo ""
echo "==========================================="
echo "SETTINGS"
echo "==========================================="
echo "SELENIUM HUB SERVER      : $JARFILE"
echo "SELENIUM HUB SERVER PORT : $PORT"
echo ""

echo "==========================================="
echo "SELENIUM GRID - HUB COMMAND"
echo "==========================================="
echo $SELENIUM_SERVER_COMMAND
echo ""

eval $SELENIUM_SERVER_COMMAND
