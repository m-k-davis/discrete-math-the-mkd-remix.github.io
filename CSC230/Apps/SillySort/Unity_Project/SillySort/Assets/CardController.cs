﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class CardController : MonoBehaviour
{
    public Text num, reveal;
    bool isHidden;
    public int value;

    GameObject cancelSwapGO;

    // Start is called before the first frame update
    void Start()
    {
        isHidden = true;
        int i = transform.GetSiblingIndex();
        value = GameMan.numList[i];
        cancelSwapGO = transform.Find("CancelSwap").gameObject;
        cancelSwapGO.SetActive(false);
    }

    // Update is called once per frame
    void Update()
    {
        if(isHidden && !GameMan.gameOver)
            num.text = "?";
        else
            num.text = "" + value;

        reveal.GetComponentInParent<Button>().interactable = (!GameMan.gameOver && (
            GameMan.numRevealed < GameMan.maxRevealed || !isHidden));

        transform.Find("Swap").GetComponent<Button>().interactable =
            (!GameMan.gameOver &&  GameMan.swapA != transform);
    }

    public void revealToggle()
    {
        if (isHidden)
        {
            if (GameMan.numRevealed < GameMan.maxRevealed)
            {
                GameMan.totalNumShows++;
                GameMan.numRevealed++;
                isHidden = false;
                reveal.text = "HIDE";
            }
        }
        else
        {
            GameMan.numRevealed--;
            isHidden = true;
            reveal.text = "SHOW";
        }
    }

    public void swap()
    {
        if (GameMan.swapA == null)
        {
            GameMan.swapA = transform;
            cancelSwapGO.SetActive(true);
        }
        else
        {
            int a = GameMan.swapA.GetSiblingIndex();
            int b = transform.GetSiblingIndex();
            GameMan.swapA.SetSiblingIndex(b);
            transform.SetSiblingIndex(a);

            GameMan.swapA.GetComponent<CardController>().cancelSwapGO.SetActive(false);
            GameMan.swapA = null;

            GameMan.checkWin(transform.parent);
            cancelSwapGO.SetActive(false);

        }
    }

    public void cancelSwap()
    {
        if (GameMan.swapA != transform)
            throw new System.Exception("Can not cancel this swap");
        GameMan.swapA = null;
        cancelSwapGO.SetActive(false);
    }
}
