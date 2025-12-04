
// Navbar blur effect
document.addEventListener("scroll", function() {
        const nav = document.querySelector(".navbar-blur");
        if (!nav) return;
        if (window.scrollY > 50) {
                nav.style.background = "rgba(255, 255, 255, 0.6)";
                nav.style.backdropFilter = "blur(15px)";
                nav.style.webkitBackdropFilter = "blur(15px)";
        } else {
                nav.style.background = "rgba(255, 255, 255, 0.1)";
                nav.style.backdropFilter = "blur(0px)";
                nav.style.webkitBackdropFilter = "blur(0px)";
        }
});

// About boxes animation on scroll
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top < window.innerHeight - 80 &&
        rect.bottom > 0
    );
}

function animateAboutBoxes() {
    const boxes = document.querySelectorAll('.about-box');
    boxes.forEach((box, idx) => {
        if (isInViewport(box)) {
            setTimeout(() => {
                box.classList.add('show-animate');
            }, idx * 250);
        }
    });
}

window.addEventListener('scroll', animateAboutBoxes);
document.addEventListener('DOMContentLoaded', animateAboutBoxes);


    // إظهار الأزرار بعد اختيار نوع الشركة
    const companyTypeSelect = document.querySelector('select[name="company_type"]');
    const btnInstant = document.getElementById('btn-instant');
    const btnHire = document.getElementById('btn-hire');
    const instantSection = document.getElementById('instant-section');
    const hireSection = document.getElementById('hire-section');
    const requestTypeInput = document.getElementById('request_type_input');

    function resetSections() {
        instantSection.style.display = 'none';
        hireSection.style.display = 'none';
        requestTypeInput.value = '';
        btnInstant.classList.remove('btn-primary');
        btnInstant.classList.add('btn-outline-primary');
        btnHire.classList.remove('btn-success');
        btnHire.classList.add('btn-outline-success');
    }

    companyTypeSelect.addEventListener('change', function() {
        if (companyTypeSelect.value) {
            btnInstant.disabled = false;
            btnHire.disabled = false;
        } else {
            btnInstant.disabled = true;
            btnHire.disabled = true;
            resetSections();
        }
    });

    btnInstant.addEventListener('click', function() {
        instantSection.style.display = 'block';
        hireSection.style.display = 'none';
        requestTypeInput.value = 'instant';
        btnInstant.classList.add('btn-primary');
        btnInstant.classList.remove('btn-outline-primary');
        btnHire.classList.remove('btn-success');
        btnHire.classList.add('btn-outline-success');
    });
    btnHire.addEventListener('click', function() {
        instantSection.style.display = 'none';
        hireSection.style.display = 'block';
        requestTypeInput.value = 'hire';
        btnHire.classList.add('btn-success');
        btnHire.classList.remove('btn-outline-success');
        btnInstant.classList.remove('btn-primary');
        btnInstant.classList.add('btn-outline-primary');
    });

    // عند تحميل الصفحة، عطل الأزرار وأخفي الحقول
    window.addEventListener('DOMContentLoaded', function() {
        btnInstant.disabled = true;
        btnHire.disabled = true;
        resetSections();
    });
