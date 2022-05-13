pipeline {
  agent {
    docker {
      image 'mcr.microsoft.com/playwright:v1.21.0-focal'
    }
  }
  stages {
    stage('install playwright') {
      steps {
        sh '''
          pip install playwright
          playwright install
          pip install pytest-playwright
        '''
      }
    }
    stage('test') {
      steps {
        sh '''
          pytest -s -v --tb=short -m auth
        '''
        }
      }
    }
  }
