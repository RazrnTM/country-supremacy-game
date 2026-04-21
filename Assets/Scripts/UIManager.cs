using UnityEngine;
using UnityEngine.UI;

public class UIManager : MonoBehaviour
{
    public GameObject citiesPanel;
    public GameObject unitsPanel;
    public GameObject armyStacksPanel;

    void Start()
    {
        HideAllPanels(); // Hide all panels on start
    }

    public void ShowCitiesPanel()
    {
        HideAllPanels();
        citiesPanel.SetActive(true);
    }

    public void ShowUnitsPanel()
    {
        HideAllPanels();
        unitsPanel.SetActive(true);
    }

    public void ShowArmyStacksPanel()
    {
        HideAllPanels();
        armyStacksPanel.SetActive(true);
    }

    private void HideAllPanels()
    {
        citiesPanel.SetActive(false);
        unitsPanel.SetActive(false);
        armyStacksPanel.SetActive(false);
    }
}