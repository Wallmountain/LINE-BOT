init_menu = {
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://assets.webiconspng.com/uploads/2016/11/business_coin_currency_graphic_line_money_set_icon_1142915.png",
        "size": "5xl",
        "gravity": "top",
        "aspectMode": "cover",
        "offsetTop": "none",
        "offsetBottom": "xl",
        "offsetStart": "none",
        "offsetEnd": "none",
        "margin": "none"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "menu",
          "text": "menu"
        },
        "style": "primary",
        "height": "md",
        "position": "relative",
        "margin": "none",
        "gravity": "top",
        "adjustMode": "shrink-to-fit",
        "color": "#dd4009"
      }
    ]
  },
  "styles": {
    "header": {
      "separator": True
    },
    "hero": {
      "separator": False
    },
    "body": {
      "separator": False
    }
  }
}

main_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://ibw.bwnet.com.tw/image/pool/2019/05/95f6e6c5f75774567ce8534b3e42190e.jpg"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "xs",
        "contents": [
          {
            "type": "text",
            "text": "Introduce each function in this LINE BOT",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "message",
              "label": "see introduce",
              "text": "introduce"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://www.reipropertymanagement.net/wp-content/uploads/2019/11/bank-getty.jpg"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "wrap": True,
            "weight": "bold",
            "size": "xl",
            "text": "exchange rate in each bank"
          },
          {
            "type": "box",
            "layout": "baseline",
            "flex": 1,
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "flex": 2,
            "style": "primary",
            "color": "#aaaaaa",
            "action": {
              "type": "message",
              "label": "select bank",
              "text": "bank"
            }
          }
        ]
      }
    },
  ]
}
introduce_box = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://ibw.bwnet.com.tw/image/pool/2019/05/95f6e6c5f75774567ce8534b3e42190e.jpg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://linecorp.com"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "action": {
      "type": "uri",
      "uri": "https://linecorp.com"
    },
    "contents": [
      {
        "type": "text",
        "text": "Introduce",
        "size": "xl",
        "weight": "bold"
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_regular_32.png"
              },
              {
                "type": "text",
                "text": "exchange rate",
                "weight": "bold",
                "margin": "sm",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "choose bank and select Currency",
                "size": "sm",
                "color": "#aaaaaa",
                "align": "end"
              }
            ]
          },
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "color": "#905c44",
        "action": {
          "type": "message",
          "label": "return menu",
          "text": "menu"
        }
      }
    ]
  }
}
bank_select = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://pbs.twimg.com/media/EHlOSPQWwAAhpwW?format=jpg&name=small",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": " select bank",
        "weight": "bold",
        "size": "xl",
        "align": "start"
      },
      {
        "type": "text",
        "text": "keyboard in bank name",
        "size": "sm",
        "color": "#aaaaaa",
        "align": "start"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "return menu",
          "text": "menu"
        }
      }
    ],
    "flex": 0
  }
}

Currency_select_for_value_now = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.bankrate.com/2020/06/02131848/Meir-Jacob-Getty.jpeg?auto=webp&optimize=high&crop=16:9",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    },
    "margin": "none"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "select Currency type",
        "weight": "bold",
        "size": "xl",
        "align": "start"
      },
      {
        "type": "text",
        "text": "keyboard in Currency type",
        "size": "sm",
        "color": "#aaaaaa"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "value",
          "label": "return select display method"
        },
        "color": "#aabbff"
      }
    ],
    "flex": 0
  }
}

display_method = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://media.gettyimages.com/vectors/coin-icon-on-transparent-background-vector-id1283073161?k=20&m=1283073161&s=612x612&w=0&h=l3RCmQNcwSP5dBBAbucGGVBeiOKG-j1TIlxXXDXHy1Y=",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    },
    "margin": "none"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": " select display method",
        "weight": "bold",
        "size": "xl",
        "align": "start"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "Real-time Exchange rate",
          "text": "value_now"
        },
        "color": "#ffbbaa"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "text": "value_recently",
          "label": "Run chart"
        },
        "style": "primary",
        "height": "sm",
        "color": "#bbaaff"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "return select bank",
          "text": "bank"
        },
        "style": "primary",
        "height": "sm",
        "color": "#aabbff"
      }
    ],
    "flex": 0
  }
}
show_value_now = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.bankrate.com/2020/06/02131848/Meir-Jacob-Getty.jpeg?auto=webp&optimize=high&crop=16:9",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    },
    "margin": "none"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "weight": "bold",
        "size": "xl",
        "align": "start",
        "text": "匯率"
      },
      {
        "type": "separator"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "銀行",
            "size": "xl"
          },
          {
            "type": "text",
            "size": "xl",
            "text": "台灣銀行",
            "align": "end",
            "margin": "none"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "幣別",
            "size": "xl"
          },
          {
            "type": "text",
            "size": "xl",
            "text": "USD",
            "align": "end",
            "margin": "none"
          }
        ]
      },
      {
        "type": "separator"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "size": "xl",
            "text": "現金買入"
          },
          {
            "type": "text",
            "size": "xl",
            "align": "end",
            "margin": "none",
            "text": "0.00"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "現金賣出",
            "size": "xl"
          },
          {
            "type": "text",
            "size": "xl",
            "text": "0.00",
            "align": "end",
            "margin": "none"
          }
        ]
      },
      {
        "type": "separator"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "即期買入",
            "size": "xl"
          },
          {
            "type": "text",
            "size": "xl",
            "text": "0.00",
            "align": "end",
            "margin": "none"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "即期賣出",
            "size": "xl"
          },
          {
            "type": "text",
            "size": "xl",
            "text": "0.00",
            "align": "end",
            "margin": "none"
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "value_now",
          "label": "return select Currency type"
        },
        "color": "#aabbff"
      }
    ],
    "flex": 0
  }
}

value_recently = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://elt.rti.org.tw/wp-content/uploads/2018/03/960x540_learning-english-qa-table-diagram-graph-chart-imagesgetty.jpg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    },
    "margin": "none"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "weight": "bold",
        "size": "xl",
        "align": "start",
        "text": "select time interval"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "value_3month",
          "label": "3 month"
        },
        "color": "#aabbff"
      },
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "value_6month",
          "label": "6 month"
        },
        "color": "#bbbbff"
      },
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "value",
          "label": "return select display method"
        },
        "color": "#bbffbb"
      }
    ],
    "flex": 0
  }
}

select_currency_value_recently = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://cdn.corporatefinanceinstitute.com/assets/currency-1024x682.jpeg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "fit",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    },
    "margin": "none"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "weight": "bold",
        "size": "xl",
        "align": "start",
        "text": "select Currency type"
      },
      {
        "type": "text",
        "text": "keyboard in Currency type",
        "size": "sm",
        "color": "#aaaaaa",
        "align": "start"
      }
    ],
    "spacing": "none"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "value_recently",
          "label": "return select time intervel"
        },
        "color": "#aabbff"
      }
    ],
    "flex": 0
  }
}

show_value_3month = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_3_movie.png",
        "size": "full",
        "aspectMode": "fit",
        "action": {
            "type": "uri",
            "uri": "http://linecorp.com/"
        },
        "margin": "none"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "three-month trend chart",
            "size": "xl",
            "weight": "bold"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "bank"
              },
              {
                "type": "text",
                "text": "-",
                "color": "#aaaaaa",
                "align": "start"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Currency type"
              },
              {
                "type": "text",
                "text": "-",
                "color": "#aaaaaa",
                "align": "start"
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "return select Currency type",
              "text": "value_3month"
            },
            "style": "primary",
            "height": "sm",
            "color": "#aabbff"
          }
        ]
      },
      "size": "giga"
    }
  ]
}
