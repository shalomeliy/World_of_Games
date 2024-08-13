pipeline {
    agent any

    environment {
        VERSION_FILE = 'version.txt'
        DOCKER_IMAGE_BASE = 'shalomeliy/main_score'
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
        stage('Read Version') {
            steps {
                dir('World_of_Games') {
                script {
                        def version = readFile(VERSION_FILE).trim() 
                        env.IMAGE_VERSION = version // Store the version in an environment variable
                        echo "Version is ${env.IMAGE_VERSION}"
                        }
                    }
                }
            }
 stage('Build Docker') {
    steps {
        dir('World_of_Games') {
            script {
                if (isUnix()) {
                    sh "export IMAGE_VERSION=${env.IMAGE_VERSION} && docker-compose build"
                    echo "Versionme is ${env.IMAGE_VERSION}"
                    sh "docker-compose up -d"
                } else {
                    bat "set IMAGE_VERSION=${env.IMAGE_VERSION} && docker-compose build"
                    echo "Versionme is ${env.IMAGE_VERSION}"
                    bat "docker-compose up -d"
                }
            }
        }
    }
}
stage('Verify Tags') {
    steps {
        script {
            if (isUnix()) {
                sh "docker images"
            } else {
                bat "docker images"
            }
        }
    }
}

stage('Tag & Push Docker Image') {
    steps {
        script {
            def imageVersion = env.IMAGE_VERSION
            if (isUnix()) {
              
                sh bat "docker push $DOCKER_IMAGE_BASE:${imageVersion}"
            } else {
                bat bat "docker push $DOCKER_IMAGE_BASE:${imageVersion}"
            }
        }
    }
}


        stage('Increment Version') {
            steps {
                script {
                    def version = readFile(VERSION_FILE).trim().toInteger() + 1
                    writeFile file: VERSION_FILE, text: version.toString()
                    echo "Incremented version to ${version}"
                }
            }
        }
        stage('E2E Test') {
            steps {
                dir('World_of_Games') {
                    script {
                        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                            if (isUnix()) {
                                sh 'python tests/e2e.py'
                            } else {
                                bat 'python tests/e2e.py'
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
                        } else {
                            bat 'docker-compose down'
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
