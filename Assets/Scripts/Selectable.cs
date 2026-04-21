using UnityEngine;

// Enum to define selectable types
public enum SelectableType
{
    Character,
    Item,
    Environment
}

public class Selectable : MonoBehaviour
{
    public SelectableType selectableType;
    private bool isSelected;

    // Method to select the object
    public void OnSelect()
    {
        isSelected = true;
        Highlight(true);
        GetDetails(); // Optionally retrieve details when selected
    }

    // Method to deselect the object
    public void OnDeselect()
    {
        isSelected = false;
        Highlight(false);
    }

    // Method to highlight the object
    private void Highlight(bool value)
    {
        // Implement highlight logic here (e.g. change color, outline, etc.)
    }

    // Method to get details about the selectable object
    public void GetDetails()
    {
        // Implement logic to retrieve details of the object
        Debug.Log("Object Type: " + selectableType);
    }
}