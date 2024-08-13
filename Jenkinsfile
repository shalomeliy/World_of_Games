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
                script {
                    if (fileExists(VERSION_FILE)) {
                        def version = readFile(VERSION_FILE).trim()
                        if (version.isEmpty()) {
                            writeFile(file: VERSION_FILE, text: "1")
                            env.IMAGE_VERSION = "1"
                            echo "Version file was empty. Updated file with version ${env.IMAGE_VERSION}"
                        } else {
                            env.IMAGE_VERSION = version
                            echo "Current version is ${env.IMAGE_VERSION}"
                        }
                    } else {
                        writeFile(file: VERSION_FILE, text: "1")
                        env.IMAGE_VERSION = "1"
                        echo "Version file did not exist. Created new file with version ${env.IMAGE_VERSION}"
                    }
                }
            }
        }
        stage('Build Docker') {
    steps {
        dir('World_of_Games') {
            script {
                if (isUnix()) {
                    sh "ls -al" // List files to verify docker-compose.yml is present
                    sh """
                    export IMAGE_VERSION=${env.IMAGE_VERSION}
                    docker-compose up --build -d
                    """
                } else {
                    bat "dir" // List files to verify docker-compose.yml is present
                    bat """
                    set IMAGE_VERSION=${env.IMAGE_VERSION}
                    docker-compose up --build -d
                    """
                }
            }
        }
    }
}

        stage('Tag & Push Docker Image') {
            steps {
                script {
                    def imageVersion = env.IMAGE_VERSION
                    if (isUnix()) {
                        sh "docker tag ${DOCKER_IMAGE_BASE}:${imageVersion} ${DOCKER_IMAGE_BASE}:${imageVersion}"
                        sh "docker push ${DOCKER_IMAGE_BASE}:${imageVersion}"
                    } else {
                        bat "docker tag ${DOCKER_IMAGE_BASE}:${imageVersion} ${DOCKER_IMAGE_BASE}:${imageVersion}"
                        bat "docker push ${DOCKER_IMAGE_BASE}:${imageVersion}"
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
