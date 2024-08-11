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
        stage('Increment Version') {
            steps {
                dir('World_of_Games') {
                    script {
                        def versionFile = 'version.txt'
                        def version = ''

                        // Read the version file
                        if (isUnix()) {
                            version = sh(script: "cat ${versionFile}", returnStdout: true).trim()
                        } else {
                            version = bat(script: "type ${versionFile}", returnStdout: true).trim()
                        }

                        // Increment the minor version
                        def (major, minor) = version.tokenize('.')
                        minor = (minor.toInteger() + 1).toString()
                        version = "${major}.${minor}"

                        // Write the new version back to the file
                        if (isUnix()) {
                            sh "echo ${version} > ${versionFile}"
                        } else {
                            bat "echo ${version} > ${versionFile}"
                        }

                        // Update the DOCKER_IMAGE environment variable
                        env.DOCKER_IMAGE = "${DOCKER_IMAGE_BASE}:${version}"
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
        stage('Tag & Push Docker Image') {
            steps {
                script {
                    if (isUnix()) {
                        sh "docker tag ${DOCKER_IMAGE} ${DOCKER_IMAGE_BASE}:latest"
                        sh "docker push ${DOCKER_IMAGE}"
                        sh "docker push ${DOCKER_IMAGE_BASE}:latest"
                    } else {
                        bat "docker tag ${DOCKER_IMAGE} ${DOCKER_IMAGE_BASE}:latest"
                        bat "docker push ${DOCKER_IMAGE}"
                        bat "docker push ${DOCKER_IMAGE_BASE}:latest"
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
