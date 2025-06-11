document.addEventListener('DOMContentLoaded', function () {
    // Get the category and subcategory fields
    const categoryField = document.querySelector('#id_category');
    const subCategoryField = document.querySelector('#id_sub_category');

    // Ensure both fields exist
    if (!categoryField || !subCategoryField) {
        console.error('Category or Subcategory field not found.');
        return;
    }

    // Parse the categories data from the category field's data attribute
    let categories;
    try {
        categories = JSON.parse(categoryField.getAttribute('data-categories'));
    } catch (error) {
        console.error('Failed to parse categories data:', error);
        categories = {};
    }

    // Function to update the subcategory options
    function updateSubcategories(selectedCategory) {
        const subCategories = categories[selectedCategory] || [];
        subCategoryField.innerHTML = ''; // Clear existing options

        // Add new options to the subcategory dropdown
        subCategories.forEach(subCategory => {
            const option = document.createElement('option');
            option.value = subCategory;
            option.textContent = subCategory;
            subCategoryField.appendChild(option);
        });

        // Add a default "Other" option if no subcategories exist
        if (subCategories.length === 0) {
            const option = document.createElement('option');
            option.value = 'Other';
            option.textContent = 'Other';
            subCategoryField.appendChild(option);
        }
    }

    // Event listener for category field changes
    categoryField.addEventListener('change', function () {
        updateSubcategories(this.value);
    });

    // Trigger the change event on page load to populate subcategories if editing an existing product
    updateSubcategories(categoryField.value);
});