pipeline {
    agent any

    environment {
        DOCKER_IMAGE_BASE = 'shalomeliy/world_of_games'
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
 stage('Read and Increment Build Number') {
            steps {
                script {
                    def versionsFile = 'World-Of-Games/version.txt'
                    
                    // Read the current build number
                    def currentBuildNumber = 0
                    if (fileExists(versionsFile)) {
                        currentBuildNumber = readFile(versionsFile).trim().toInteger()
                    }
                    
                    // Increment the build number
                    def newBuildNumber = currentBuildNumber + 1
                    
                    // Write the new build number back to the file
                    writeFile file: versionsFile, text: "${newBuildNumber}"
                    
                    // Set the new build number as an environment variable for use in Docker tag
                    env.BUILD_NUMBER = newBuildNumber.toString()
                    env.IMAGE_TAG = newBuildNumber.toString()
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
//        stage('Tag & Push Docker Image') {
//            steps {
//                script {
//                    if (isUnix()) {
//                        sh "docker tag ${DOCKER_IMAGE_BASE}:${env.VERSION} ${DOCKER_IMAGE_BASE}:latest"
//                        sh "docker push ${DOCKER_IMAGE_BASE}:${env.VERSION}"
//                        sh "docker push ${DOCKER_IMAGE_BASE}:latest"
//                    } else {
//                        bat "docker tag ${DOCKER_IMAGE_BASE}:${env.VERSION} ${DOCKER_IMAGE_BASE}:latest"
//                        bat "docker push ${DOCKER_IMAGE_BASE}:${env.VERSION}"
//                        bat "docker push ${DOCKER_IMAGE_BASE}:latest"
//                    }
//                }
//            }
//        }
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
