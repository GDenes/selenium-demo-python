@echo off
TITLE "Selenium Node settings - connection to hub"

SET CHROME=
SET FIREFOX=
SET EDGE=

for %%i in (chrome*.*) do SET CHROME=%%i
for %%i in (gecko*.*) do SET FIREFOX=%%i
for %%i in (*edge*.*) do SET EDGE=%%i
SET REMOTEIP=http://127.0.0.1:4444
for %%i in (*.jar) do SET JARFILE=%%i

SET selenium_server_command=java
SET browser_settings=

goto getOpts

:getOpts
if /I "%1" == "-h" goto :Help
if /I "%1" == "--chromedriver" set CHROME=%2 & shift
if /I "%1" == "--geckodriver" set FIREFOX=%2 & shift
if /I "%1" == "--edgedriver" set EDGE=%2 & shift
if /I "%1" == "--remoteip" set REMOTEIP=%2 & shift
if /I "%1" == "-f" set JARFILE=%2 & shift
shift
if not "%1" == "" goto getOpts

call :setCommandVariables

call :createCommand

call :printSettings

%selenium_server_command%

:setCommandVariables
if %CHROME% NEQ ""  (
	SET selenium_server_command=%selenium_server_command% -Dwebdriver.chrome.driver="%CHROME%"
	SET browser_chrome_max_instance="browserName=chrome,maxInstances=5"
	SET browser_settings=%browser_settings% -browser %browser_chrome_max_instance%
)

if %FIREFOX% NEQ "" (
	SET selenium_server_command=%selenium_server_command% -Dwebdriver.gecko.driver="%FIREFOX%"
	SET browser_firefox_max_instance="browserName=firefox,maxInstances=5"
	SET browser_settings=%browser_settings% -browser %browser_firefox_max_instance%
)

if %EDGE% NEQ "" (
	SET selenium_server_command=%selenium_server_command% -Dwebdriver.edge.driver="%EDGE%"
	SET browser_edge_max_instance="browserName=MicrosoftEdge,maxInstances=5"
	SET browser_settings=%browser_settings% -browser %browser_edge_max_instance%
)

if %JARFILE% NEQ "" (SET selenium_server_command=%selenium_server_command% -jar %JARFILE%) else (echo "Please check current directory, because no have executable .jar file!")

goto :eof

:createCommand
SET selenium_server_command=%selenium_server_command% %browser_settings%
SET REGISTER_STRING= -role node -hub 
SET selenium_server_command=%selenium_server_command%%REGISTER_STRING%%REMOTEIP%/grid/register
goto :eof

:: Print setted settings
:printSettings
echo.
echo ===========================================
echo SETTINGS
echo ===========================================
echo CHROME DRIVER  : %CHROME%
echo FIREFOX DRIVER : %FIREFOX%
echo EDGE DRIVER    : %EDGE%
echo REMOTE IP      : %REMOTEIP%
echo SELENIUM GRID  : %JARFILE%
echo.

echo ===========================================
echo SELENIUM GRID - REGISTER NODE COMMAND
echo ===========================================
echo %selenium_server_command%
echo.
goto :eof

::Help function
:Help
echo.
echo ===========================================
echo COMMAND PARAMETER HELP
echo ===========================================
echo [ --chromedriver ] - Chrome driver path
echo [ --edgedriver ]   - Edge driver path
echo [ --geckodriver ]  - Gecko driver path
echo [ --remoteip ]     - Remote Selenium grid register url with port
echo [ -f ]             - Selenium standalone server ".jar" file path
goto :eof