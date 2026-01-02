pipeline {
    agent any

    environment {
        IMAGE_NAME    = "amoghlokhande/myapp"
        IMAGE_TAG     = "${BUILD_NUMBER}"
        DEPLOY_REPO   = "deploy-repo"
        DEPLOY_BRANCH = "main"
    }

    stages {
        stage("Checkout App Code") {
            steps {
                checkout scm
            }
        }
        stage("SonarQube Analysis") {
            steps {
                script {
                    def scannerHome = tool 'sonar-scanner'
                    withSonarQubeEnv('sonar-scanner') {
                        sh """
                          ${scannerHome}/bin/sonar-scanner \
                          -Dsonar.projectKey=fluxgate-app \
                          -Dsonar.sources=my-app \
                          -Dsonar.language=py
                        """
                    }
                }
            }
        }

        stage("Build Docker Image") {
            steps {
                sh """
                  docker build \
                    -t ${IMAGE_NAME}:${IMAGE_TAG} \
                    my-app
                """
            }
        }

        stage("Trivy Scan") {
            steps {
                sh """
                  trivy image --exit-code 0 \
                  ${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }


        stage("Push Docker Image") {
            steps {
                withDockerRegistry(
                    credentialsId: 'dockerhub-credentials',
                    url: 'https://index.docker.io/v1/'
                ) {
                    sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }


        stage("Update Deploy Repo (GitOps)") {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'git-cred',
                        usernameVariable: 'GIT_USER',
                        passwordVariable: 'GIT_TOKEN'
                    )
                ]) {
                    sh '''
                      rm -rf deploy-repo

                      git clone https://github.com/Amogh052003/deploy-repo.git
                      cd deploy-repo

                      git config user.email "jenkins@fluxgate.io"
                      git config user.name  "jenkins-bot"

                      sed -i "s|image: .*|image: ${IMAGE_NAME}:${IMAGE_TAG}|" environments/dev/image.yaml

                      git add environments/dev/image.yaml
                      git commit -m "chore(dev): deploy ${IMAGE_NAME}:${IMAGE_TAG}"

                      git push https://$GIT_USER:$GIT_TOKEN@github.com/Amogh052003/deploy-repo.git ${DEPLOY_BRANCH}
                    '''
                }
            }
        }
    }

    post {
        success {
            echo " Pipeline succeeded – image pushed & GitOps repo updated"
        }
        failure {
            echo " Pipeline failed"
        }
        always {
            echo "======== Pipeline Finished ========"
        }
    }
}
