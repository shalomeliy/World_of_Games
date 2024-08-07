pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'shalomeliy/main_score:1.0'
    }

    stages {
        stage('Clean Up') {
            steps {
                deleteDir()
            }
        }
        stage('Clone Repo') {
            steps {
                script {
                    if (isUnix()) {
                        sh "git clone https://github.com/shalomeliy/World_of_Games.git"
                    } else {
                        bat "git clone https://github.com/shalomeliy/World_of_Games.git"
                    }
                }
            }
        }
        stage('Print Disk Space') {
            steps {
                script {
                    if (!isUnix()) {
                        def scriptText = '''
                        $disk = Get-PSDrive -Name C
                        Write-Output "Free space on C: $([math]::round($disk.Free/1GB, 2)) GB"
                        '''
                        writeFile file: 'diskfree.ps1', text: scriptText
                        bat 'powershell.exe -File diskfree.ps1'
                    } else {
                        sh 'df -h'
                    }
                }
            }
        }
        stage('Install Requirements') {
            steps {
                dir('World_of_Games') {
                    script {
                        if (isUnix()) {
                            sh "pip install -r requirements.txt"
                        } else {
                            bat "pip install -r requirements.txt"
                        }
                    }
                }
            }
        }
        stage('Build Docker') {
            steps {
                dir('World_of_Games') {
                    script {
                        if (isUnix()) {
                            sh "docker-compose up --build -d"
                        } else {
                            bat "docker-compose up --build -d"
                        }
                    }
                }
            }
        }
        stage('E2E Test') {
            steps {
                dir('World_of_Games') {
                    script {
                        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                            if (isUnix()) {
                                sh 'python e2e.py'
                            } else {
                                bat 'python e2e.py'
                            }
                        }
                    }
                }
            }
        }
        stage('Finalize') {
            steps {
                dir('World_of_Games') {
                    script {
                        if (isUnix()) {
                            sh 'docker-compose down'
                            sh "docke push $DOCKER_IMAGE"
                        } else {
                            bat 'docker-compose down'
                            bat "docke push $DOCKER_IMAGE"
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
