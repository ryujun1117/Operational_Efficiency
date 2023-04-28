/////////////// カレンダ設定 ///////////////////
// 予定の作成
// Creates an all-day event for the moon landing and logs the ID.
function create_cal(){
var event = CalendarApp.getDefaultCalendar().createAllDayEvent('test',
    new Date('April 28, 2023'));
Logger.log('Event ID: ' + event.getId());
}


/////////////// task機能 //////////////////////

/**
 * Lists the titles and IDs of tasksList.
 * @see https://developers.google.com/tasks/reference/rest/v1/tasklists/list
 */
function listTaskLists() {
  try {
    // Returns all the authenticated user's task lists.
    const taskLists = Tasks.Tasklists.list();
    // If taskLists are available then print all tasklists.
    if (!taskLists.items) {
      console.log('No task lists found.');
      return;
    }
    // Print the tasklist title and tasklist id.
    for (let i = 0; i < taskLists.items.length; i++) {
      const taskList = taskLists.items[i];
      console.log('Task list with title "%s" and ID "%s" was found.', taskList.title, taskList.id);
    }
  } catch (err) {
    // TODO (developer) - Handle exception from Task API
    console.log('Failed with an error %s ', err.message);
  }
}
// return
// Task list with title "マイタスク" and ID "MDgzNjE2MjU3ODUzMjI5OTcyMzg6MDow" was found.

//////////////////////////////////////////////////////////////////////////////////////////////////

/**
 * Lists task items for a provided tasklist ID.
 * @param  {string} taskListId The tasklist ID.
 * @see https://developers.google.com/tasks/reference/rest/v1/tasks/list
 */
function listTasks(taskListId = "MDgzNjE2MjU3ODUzMjI5OTcyMzg6MDow") {
  try {
    // List the task items of specified tasklist using taskList id.
    const tasks = Tasks.Tasks.list(taskListId);
    // If tasks are available then print all task of given tasklists.
    if (!tasks.items) {
      console.log('No tasks found.');
      return;
    }
    // Print the task title and task id of specified tasklist.
    for (let i = 0; i < tasks.items.length; i++) {
      const task = tasks.items[i];
      console.log('Task with title "%s" and ID "%s" was found.', task.title, task.id);
    }
  } catch (err) {
    // TODO (developer) - Handle exception from Task API
    console.log('Failed with an error %s', err.message);
  }
}
// return 
//Task with title "test" and ID "eWZsUWdYZmczZlNKQzdwOQ" was found.

////////////////////////////////////////////////////////////////////////////////////////////////////
// 「マイタスク」にタスクを追加する
/**
 * Adds a task to a tasklist.
 * @param {string} taskListId The tasklist to add to.
 * @see https://developers.google.com/tasks/reference/rest/v1/tasks/insert
 */
function addTask(taskListId = "MDgzNjE2MjU3ODUzMjI5OTcyMzg6MDow") {
  // Task details with title and notes for inserting new task
  let task = {
    title: 'Pick up dry cleaning',
    notes: 'Remember to get this done!'
  };
  try {
    // Call insert method with taskDetails and taskListId to insert Task to specified tasklist.
    task = Tasks.Tasks.insert(task, taskListId);
    // Print the Task ID of created task.
    console.log('Task with ID "%s" was created.', task.id);
  } catch (err) {
    // TODO (developer) - Handle exception from Tasks.insert() of Task API
    console.log('Failed with an error %s', err.message);
  }
}


