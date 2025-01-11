document.addEventListener("DOMContentLoaded", () => {
  // Get the current URL path
  const currentPath = window.location.pathname;

  // Select all nav links
  const navLinks = document.querySelectorAll(".nav-link");

  // Loop through each nav link
  navLinks.forEach((link) => {
    // Check if the href of the link matches the current path
    if (link.getAttribute("href") === currentPath) {
      // Remove active class from other links if any
      navLinks.forEach((nav) => nav.classList.remove("active"));

      // Add active class to the matching link
      link.classList.add("active");
    }
  });
});

document.addEventListener("DOMContentLoaded", () => {
  // Toggle sidebar visibility on smaller screens
  const sidebar = document.getElementById("sidebar");
  const sidebarToggle = document.getElementById("sidebarToggle");
  const closeSidebar = document.getElementById("closeSidebar");

  // Open sidebar
  sidebarToggle.addEventListener("click", () => {
    sidebar.classList.toggle("hidden");
  });

  // Close sidebar
  closeSidebar.addEventListener("click", () => {
    sidebar.classList.add("hidden");
  });
});
