Your All New Floppa Pet On Your Screen! Based On The Idea Of Desktop Goose But Now Its A Floppa! Click For Money And Let Him Explore Your Whole Computer :)

<a href="https://i.jessehoekema.com/dfi" style="color: white; text-decoration: none;">
<button class="btn" style="  background-color: DodgerBlue;
  border: none;
  color: white;
  padding: 12px 30px;
  cursor: pointer;
  font-size: 20px;"><i class="fa fa-download"></i> Download For Mac</button>
</a>

  <button class="btn" style="  background-color: DodgerBlue;
  border: none;
  color: white;
  padding: 12px 30px;
  cursor: pointer;
  font-size: 20px; cursor: not-allowed;" disabled><i class="fa fa-download"></i> Download For Windows</button>

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

### Release History
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const apiUrl = 'https://api.github.com/repos/JesseHoekema/DesktopFloppa/releases';  // Replace with your repo
    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        const releasesList = document.getElementById('releases-list');
        data.forEach(release => {
          const releaseItem = document.createElement('div');
          releaseItem.classList.add('release-item');
          
          const releaseTitle = document.createElement('h3');
          releaseTitle.textContent = release.name;
          
          const releaseDesc = document.createElement('p');
          releaseDesc.textContent = release.body || 'No description available';

          const releaseLink = document.createElement('a');
          releaseLink.href = release.html_url;
          releaseLink.textContent = 'View Release';
          releaseLink.target = '_blank';

          releaseItem.appendChild(releaseTitle);
          releaseItem.appendChild(releaseDesc);
          releaseItem.appendChild(releaseLink);

          releasesList.appendChild(releaseItem);
        });
      })
      .catch(error => console.error('Error fetching releases:', error));
  });
</script>

<div id="releases-list"></div>

