pipeline {
agent any
stages {
stage('Przygotowanie') {
steps {
echo 'Sprawdzam srodowisko...'
sh 'python3 --version'
}
}
stage('Testy') {
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
echo 'Pipeline OK'
}
failure {
echo 'Pipeline NIEUDANY'
}
}
}