import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'markdown',
  standalone: true
})
export class MarkdownPipe implements PipeTransform {
  transform(value: string): string {
    if (!value) return '';
    let processed = value
      .replace(/\\\(/g, '').replace(/\\\)/g, '')
      .replace(/\\leq/g, '≤').replace(/\\ge/g, '≥')
      .replace(/\\text\{([^}]+)\}/g, '$1')
      .replace(/\\times/g, '×');

    try {
      const m = (window as any).marked;
      if (m) {
        const result = m.parse(processed);
        return typeof result === 'string' ? result : result;
      }
    } catch {}

    return processed
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/^### (.+)$/gm, '<h3>$1</h3>')
      .replace(/^## (.+)$/gm, '<h2>$1</h2>')
      .replace(/^# (.+)$/gm, '<h1>$1</h1>')
      .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
      .replace(/`([^`]+)`/g, '<code>$1</code>')
      .replace(/^- (.+)$/gm, '<li>$1</li>')
      .replace(/(<li>.*<\/li>\n?)+/g, '<ul>$&</ul>')
      .replace(/\n{2,}/g, '</p><p>')
      .replace(/\n/g, '<br>')
      .replace(/^(.+)$/gm, (m: string) => {
        if (m.startsWith('<')) return m;
        return m;
      });
  }
}
