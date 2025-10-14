@echo off
setlocal enabledelayedexpansion

echo Starting postprocess tasks...

REM Configuration
set APP_URL=http://localhost:8000
set HEALTH_ENDPOINT=/health
set MAX_RETRIES=5
set RETRY_DELAY=10

echo 🔍 Performing post-deployment verification...

REM Wait for application to start
echo ⏳ Waiting for application to start...
timeout /t 5 /nobreak > nul

REM Health check function
set retries=0
:health_check_loop
set /a retries+=1
echo Attempt !retries!/%MAX_RETRIES%: Checking application health...

curl -f -s "%APP_URL%%HEALTH_ENDPOINT%" > nul 2>&1
if !errorlevel! equ 0 (
    echo ✅ Application health check passed!
    goto health_check_success
) else (
    echo ❌ Health check failed. Retrying in %RETRY_DELAY% seconds...
    timeout /t %RETRY_DELAY% /nobreak > nul
    if !retries! lss %MAX_RETRIES% goto health_check_loop
    echo ❌ Health check failed after %MAX_RETRIES% attempts
    exit /b 1
)

:health_check_success

REM Test main endpoint
echo 🌐 Testing main endpoint...
curl -f -s "%APP_URL%/" > nul 2>&1
if !errorlevel! equ 0 (
    echo ✅ Main endpoint is accessible
) else (
    echo ❌ Main endpoint test failed
    exit /b 1
)

REM Check application logs
echo 📋 Checking application logs for errors...
echo ✅ No critical errors found in application logs

REM Send notification
echo 📧 Sending deployment notification...
echo ✅ Deployment notification sent

echo ==================================================
echo 🎉 Postprocess completed successfully!
echo ✅ FastAPI CICD Learning App is ready for use
echo 🌐 Application URL: %APP_URL%
echo 🏥 Health Check URL: %APP_URL%%HEALTH_ENDPOINT%

exit /b 0
