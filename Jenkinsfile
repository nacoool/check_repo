pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                //git 'https://github.com/nacoool/check_repo.git'  // ✅ Updated Repo URL
                git branch: 'main', url: 'https://github.com/nacoool/check_repo.git'
            }
        }

        stage('Clean Previous Reports') {  // ✅ New stage to delete old reports
            steps {
                bat '''
                if exist report.html del report.html
                if exist report.xml del report.xml
                '''
            }
        }

        stage('Set Up Python') {
            Directly set up python
            // steps {
            //     bat 'python -m venv venv'
            //     //bat 'venv\\Scripts\\activate.bat && pip install -r requirements.txt'
            //     bat 'venv\\Scripts\\activate.bat'
            // }
            // Check if venv exist then skip else create.
            steps {
                script {
                    def venvExists = fileExists('venv')  // 🔥 Check if 'venv' folder exists
                    if (!venvExists) {
                        bat 'python -m venv venv'
                        bat 'venv\\Scripts\\activate.bat'
                        // bat '''
                        // python -m venv venv
                        // venv\\Scripts\\activate.bat && pip install -r requirements.txt
                        // '''
                    } else {
                        echo "✅ Virtual environment already set up. Skipping this step."
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\activate.bat && pytest --junitxml=report.xml --html=report.html' //--junitxml=report.xml -> do not want xml report to be generated
            }
        }
    }

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
// comment addition to learn rebase and squash
