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

       stage('Read and increase version Number') {
            steps {
                script {
                    def version_File = 'World_Of_Games/version.txt'
                    
                    // Read current version number
                    def currentVersionNumber = 0
                    currentVersionNumber = readFile(version_File).trim().toInteger()
                    }
                    
                    // Increment the version number
                    def newVersionNumber = currentVersionNumber + 1
                    
                    // Write the new version number back to the file
                    writeFile file: version_File, text: "${newVersionNumber}"
                    
                    // Set the new Version number as an env. variable for Docker tag
                    env.IMAGE_VERSION = newVersionNumber.toString()
                }
            }
        }

stage('Build Docker') {
    steps {
        dir('World_of_Games') {
            script {
                echo "Building Docker image with version: ${env.IMAGE_VERSION}"
                if (isUnix()) {
                    sh """
                    export IMAGE_VERSION=${env.IMAGE_VERSION}
                    export DOCKER_IMAGE_BASE=${env.DOCKER_IMAGE_BASE}
                    docker-compose build
                    docker-compose up -d
                    """
                } else {
                    bat """
                    set IMAGE_VERSION=${env.IMAGE_VERSION}
                    set DOCKER_IMAGE_BASE=${env.DOCKER_IMAGE_BASE}
                    docker-compose build
                    docker-compose up -d
                    """
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
                        sh "docker tag ${DOCKER_IMAGE_BASE}:${IMAGE_VERSION} ${DOCKER_IMAGE_BASE}:latest"
                        sh "docker push ${DOCKER_IMAGE_BASE}:${IMAGE_VERSION}"
                        sh "docker push ${DOCKER_IMAGE_BASE}:latest"
                    } else {
                        bat "docker tag ${DOCKER_IMAGE_BASE}:${IMAGE_VERSION} ${DOCKER_IMAGE_BASE}:latest"
                        bat "docker push ${DOCKER_IMAGE_BASE}:${IMAGE_VERSION}"
                        bat "docker push ${DOCKER_IMAGE_BASE}:latest"
                    }
                }
            }
        }

        stage('Increment Version') {
            steps {
                dir('World_of_Games') {
                    script {
                        def version = readFile(VERSION_FILE).trim().toInteger() + 1
                        writeFile file: VERSION_FILE, text: version.toString()
                        echo "Incremented version to ${version}"
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
