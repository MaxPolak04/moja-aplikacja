pipeline {
agent any
environment {
APLIKACJA = 'Kalkulator'
WERSJA = '2.0.0'
}
parameters {
choice(
name: 'SRODOWISKO',
choices: ['dev', 'staging', 'prod'],
description: 'Srodowisko docelowe'
)
} // test
stages {// test
stage('Info') {// test
steps {// test
echo "${env.APLIKACJA} v${env.WERSJA}"
echo "Build: ${env.BUILD_NUMBER}"
echo "Deploy na: ${params.SRODOWISKO}"
}
}
stage('Testy') {
steps {
sh 'python3 test_app.py'
}
}
stage('Budowanie') {
steps {
sh '''
mkdir -p build reports
cp app.py build/
echo "${APLIKACJA} v${WERSJA}" > build/info.txt
echo "Build: ${BUILD_NUMBER}" >> build/info.txt
echo "Raport: OK" > reports/raport.txt
'''
}
}
stage('Deploy') {
when {
expression {
params.SRODOWISKO != 'dev'
}
}
steps {
echo "Wdrazam na ${params.SRODOWISKO}..."
}
}
stage('Archiwizacja') {
steps {
archiveArtifacts artifacts: 'build/**,reports/**',
fingerprint: true
}
}
}
post {
success {
echo "SUKCES: ${env.APLIKACJA} na ${params.SRODOWISKO}"
}
failure {
echo 'BLAD! Sprawdz logi.'
}
always {
echo 'Pipeline zakonczony.'
}
}
}