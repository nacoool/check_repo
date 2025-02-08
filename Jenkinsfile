pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/nacoool/check_repo.git'  // ✅ Updated Repo URL
            }
        }

        stage('Set Up Python') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate.bat && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\activate.bat && pytest --junitxml=report.xml --html=report.html'
            }
        }

        stage('Publish Reports') {
            post {
                always {
                    junit 'report.xml'
                    publishHTML(target: [allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: '.',
                        reportFiles: 'report.html',
                        reportName: 'Test Report'
                    ])
                }
            }
        }
    }
}
