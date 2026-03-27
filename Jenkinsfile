pipeline {
agent any
stages {
stage('Info') {
steps {
echo "Galaz: ${env.GIT_BRANCH}"
echo "Build: ${env.BUILD_NUMBER}"
}
}
stage('Testy') {
when {
expression {
env.GIT_BRANCH != 'origin/main'
}
}
steps {
sh 'python3 test_app.py'
}
}
stage('Aplikacja') {
steps {
sh 'python3 app.py'
}
}
}
post {
success {
echo "OK — galaz: ${env.GIT_BRANCH}"
}
failure {
echo 'BLAD! Sprawdz logi.'
}
}
