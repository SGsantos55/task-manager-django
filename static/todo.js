document.addEventListener("DOMContentLoaded", function() {
    // Task Completion Toggle
    const todoItems = document.querySelectorAll('.todo-item');

    todoItems.forEach(item => {
        item.addEventListener('click', function() {
            const taskStatus = item.querySelector('.status');
            if (taskStatus.innerText === "⏳") {
                taskStatus.innerHTML = "✅";  // Mark as completed
                item.classList.add('completed');  // Add completed class for styling
            } else {
                taskStatus.innerHTML = "⏳";  // Mark as in-progress
                item.classList.remove('completed');  // Remove completed class
            }
            // Update Task Count
            updateTaskCounts();
        });
    });

    // Dynamic Task Count Update
    function updateTaskCounts() {
        const availableTasks = document.querySelectorAll('.todo-item:not(.completed)');
        const finishedTasks = document.querySelectorAll('.todo-item.completed');
        document.getElementById('available-tasks').innerText = availableTasks.length;
        document.getElementById('finished-tasks').innerText = finishedTasks.length;
    }

    // Initial count update
    updateTaskCounts();
});
