/* =============================================
 * 弹窗核心逻辑 + 点击计数
 * 计数数据存在 localStorage
 * 确认 = a数据，取消 = b数据
 * ============================================= */

// 兼容所有页面加载时机
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initPopup);
} else {
  initPopup();
}

function initPopup() {
  // 配置不存在则退出
  if (!window.POPUP_CONFIG) {
    console.warn('[弹窗插件] 未找到配置');
    return;
  }

  const config = window.POPUP_CONFIG;
  const storageKey = config.storageKey || 'hexo_popup_counter';

  // 读取计数
  function getCounter() {
    try {
      const data = localStorage.getItem(storageKey);
      return data ? JSON.parse(data) : { a: 0, b: 0 };
    } catch (e) {
      return { a: 0, b: 0 };
    }
  }

  // 保存计数
  function saveCounter(data) {
    try {
      localStorage.setItem(storageKey, JSON.stringify(data));
    } catch (e) {
      console.warn('[弹窗插件] 计数保存失败', e);
    }
  }

  // 只弹一次模式
  if (config.showOnce && sessionStorage.getItem('popup_shown')) {
    return;
  }

  // 创建弹窗
  createPopup();

  function createPopup() {
    console.log('[弹窗插件] 正在创建弹窗');

    // 遮罩层
    const mask = document.createElement('div');
    mask.className = 'popup-mask';

    // 弹窗主体
    const box = document.createElement('div');
    box.className = 'popup-box';
    box.style.setProperty('--popup-width', config.width || '480px');
    box.style.setProperty('--popup-max-width', config.maxWidth || '800px');

    // 板块A：文字
    const sectionA = document.createElement('div');
    sectionA.className = 'popup-section-a';
    const titleEl = document.createElement('h3');
    titleEl.className = 'popup-title';
    titleEl.textContent = config.title || '温馨提示';
    const contentEl = document.createElement('p');
    contentEl.className = 'popup-content';
    contentEl.innerHTML = config.content || '';
    sectionA.append(titleEl, contentEl);

    // 板块B：图片
    const sectionB = document.createElement('div');
    sectionB.className = 'popup-section-b';
    const images = config.images || [];
    images.forEach(function (imgUrl) {
      const img = document.createElement('img');
      img.className = 'popup-img';
      img.src = imgUrl;
      img.alt = '弹窗图片';
      sectionB.appendChild(img);
    });

    // 板块C：按钮
    const sectionC = document.createElement('div');
    sectionC.className = 'popup-section-c';

    const cancelBtn = document.createElement('button');
    cancelBtn.className = 'popup-btn popup-btn-cancel';
    cancelBtn.textContent = config.cancelText || '取消';
    cancelBtn.onclick = function () {
      const counter = getCounter();
      counter.b++;
      saveCounter(counter);
      console.log('[弹窗插件] 点击取消，当前计数', getCounter());
      closePopup();
    };

    const confirmBtn = document.createElement('button');
    confirmBtn.className = 'popup-btn popup-btn-confirm';
    confirmBtn.textContent = config.confirmText || '确认';
    confirmBtn.onclick = function () {
      const counter = getCounter();
      counter.a++;
      saveCounter(counter);
      console.log('[弹窗插件] 点击确认，当前计数', getCounter());
      closePopup();
    };

    sectionC.append(cancelBtn, confirmBtn);

    // 组装
    box.append(sectionA, sectionB, sectionC);
    mask.appendChild(box);
    document.body.appendChild(mask);

    console.log('[弹窗插件] 弹窗创建完成');

    if (config.showOnce) {
      sessionStorage.setItem('popup_shown', '1');
    }
  }

  // 关闭弹窗
  function closePopup() {
    const mask = document.querySelector('.popup-mask');
    if (!mask) return;
    mask.style.transition = 'opacity 0.2s ease';
    mask.style.opacity = '0';
    setTimeout(function () {
      mask.remove();
    }, 200);
  }

  // 暴露全局方法
  window.getPopupCounter = getCounter;
  window.resetPopupCounter = function () {
    saveCounter({ a: 0, b: 0 });
    console.log('[弹窗插件] 计数已重置');
  };
}